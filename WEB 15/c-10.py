import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

TOKEN = 'TOKEN'
LOGIN, PASSWORD = 'LOGIN', 'PASSWORD'

TOKEN = '58883f4c0d6d57119e3ebb47633b5c573f4643363613ec4b65983c8cee6fe9dfb7e0e74389eeff5d811da'

LOGIN = '89021419881'
PASSWORD = '2111Efiop'


def main():
    vk_session_api = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session_api, 204212860)
    flag = False

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW and not flag:
            send_message_hi(event)
            flag = True
        elif event.type == VkBotEventType.MESSAGE_NEW and flag:
            send_message_date(event)


def send_message_hi(event):
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk_session = vk_api.VkApi(
        token=TOKEN)
    vk = vk_session.get_api()

    vk.messages.send(user_id=event.obj.message['from_id'], message=f"Привет!",
                     random_id=random.randint(0, 2 ** 64))
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message=f"Я умею определять время по дате. Просто введи ее в формате YYYY-MM-DD",
                     random_id=random.randint(0, 2 ** 64))


def send_message_date(event):
    print(event.obj.message['text'])

    data = datetime.datetime.strptime(event.obj.message['text'], '%Y-%m-%d')

    days = {
        '0': "Понедельник",
        "1": "Вторник",
        "2": "Среда",
        "3": "Четверг",
        "4": "Пятница",
        "5": "Суббота",
        "6": "Воскресение"

    }
    print(days[str(data.weekday())])

    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk_session = vk_api.VkApi(
        token=TOKEN)
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=f"{days[str(data.weekday())]}",
                     random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
