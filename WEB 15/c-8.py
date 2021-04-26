import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

TOKEN = '58883f4c0d6d57119e3ebb47633b5c573f4643363613ec4b65983c8cee6fe9dfb7e0e74389eeff5d811da'

LOGIN = '89021419881'
PASSWORD = '2111Efiop'


def main():
    vk_session_api = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session_api, 204212860)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            send_message(event)

    vk = vk_session_api.get_api()


def send_message(event):
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.photos.get(album_id='wall', owner_id=-204212860)
    list_photos = []
    if response['items']:
        for i in response['items']:
            list_photos.append((i['owner_id'], i['id']))
    owner_id, object_id = list_photos[random.randrange(0, len(list_photos))]

    user_id = event.obj.message['from_id']
    vk_session = vk_api.VkApi(
        token=TOKEN)
    vk = vk_session.get_api()
    response = vk.users.get(user_ids=user_id, fields=['city', 'nickname'])
    print(response)
    vk.messages.send(user_id=event.obj.message['from_id'], message=f"Привет {response[0]['first_name']}!",
                     random_id=random.randint(0, 2 ** 64), attachment=f'photo{owner_id}_{object_id}')


if __name__ == '__main__':
    main()
