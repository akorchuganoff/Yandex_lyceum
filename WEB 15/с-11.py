import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard
from pprint import pprint
import datetime
import random
import os
import re
import locale
import wikipedia
import requests
import shutil

locale.setlocale(locale.LC_ALL, "ru_RU")
wikipedia.set_lang("ru")
offset = datetime.timezone(datetime.timedelta(hours=3))

users = {}
TOKEN = '58883f4c0d6d57119e3ebb47633b5c573f4643363613ec4b65983c8cee6fe9dfb7e0e74389eeff5d811da'

LOGIN = '89021419881'
PASSWORD = '2111Efiop'

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция. """

    # Код двухфакторной аутентификации,
    # который присылается по смс или уведомлением в мобильное приложение
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def geocoder_json(place):
    geocoder_request = (f"http://geocode-maps.yandex.ru/1.x/?"
                        f"apikey=40d1649f-0493-4b70-98ba-98533de7710b"
                        f"&geocode={place}&format=json")
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        return response.json()["response"]
    else:
        return None


def get_static_url(user_id):
    user = users[user_id]
    width, height = 450, 450
    json_resp = geocoder_json(user['place'])
    geo_object = json_resp["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    center = tuple(map(float, geo_object["Point"]["pos"].split()))
    lower_corner, upper_corner = map(
        lambda x: tuple(
            map(float, geo_object["boundedBy"]["Envelope"][x].split())),
        ("lowerCorner", "upperCorner"))
    static_url = (f'https://static-maps.yandex.ru/1.x/?'
                  f'l={user["l"]}&'
                  f'll={center[0]},{center[1]}&'
                  f'bbox={lower_corner[0]},{lower_corner[1]}~{upper_corner[0]},{upper_corner[1]}&'
                  f'size={width},{height}')
    return static_url


def load_image(url):
    r = requests.get(url)
    file_name = f"temp{random.randint(0, 1 << 64)}.jpg"
    with open(file_name, 'wb') as f:
        f.write(bytes(r.content))
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)
    r = upload.photo(file_name, album_id='270588491', group_id='194992614', )[0]
    return f"photo{r['owner_id']}_{r['id']}"


def main():
    token = TOKEN
    vk_session = vk_api.VkApi(token=token)
    # try:
    #     vk_session.auth(token_only=True)
    # except vk_api.AuthError as error_msg:
    #     print(error_msg)
    #     return

    longpoll = VkBotLongPoll(vk_session, '204212860')
    vk = vk_session.get_api()

    for event in longpoll.listen():
        if event.type in [VkBotEventType.MESSAGE_NEW]:
            text = event.obj.message['text']
            user_id = event.obj.message['from_id']
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', user_id)
            print('Текст:', text)

            message = "Бот предлагает ввести название местности, которую хочет увидеть пользователь"
            keyboard = VkKeyboard.get_empty_keyboard()
            user = users.setdefault(user_id, {'status': 'greeting'})
            attachment = []
            if user['status'] == 'greeting':
                print(1)
                users[user_id] = {'status': 'input'}
            elif user['status'] == 'input':
                print(2)
                message = 'Какой тип карты вы хотите увидеть?'
                user['status'] = 'l_input'
                user['place'] = text
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('map')
                keyboard.add_button('sat')
                keyboard = keyboard.get_keyboard()
            elif user['status'] == 'l_input':
                print(3)
                user['l'] = text
                message = f"Это {user['place']}. Что вы еще хотите увидеть?"
                attachment.append(load_image(get_static_url(user_id)))
                user['status'] = 'input'
            vk.messages.send(user_id=user_id,
                             message=message,
                             keyboard=keyboard,
                             attachment=attachment,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()