import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

TOKEN = '58883f4c0d6d57119e3ebb47633b5c573f4643363613ec4b65983c8cee6fe9dfb7e0e74389eeff5d811da'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 204212860)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            send_message(event)


def send_message(event):
    days = {
        '0': "Понедельник",
        "1": "Вторник",
        "2": "Среда",
        "3": "Четверг",
        "4": "Пятница",
        "5": "Суббота",
        "6": "Воскресение"

    }

    f = False
    time = ('время', 'число', 'дата', 'день')
    for elem in time:
        if elem in event.obj.message['text']:
            f = True
            break

    if f:
        moskow = datetime.timezone(datetime.timedelta(hours=3))
        data = datetime.datetime.fromtimestamp(event.obj.message['date'], tz=moskow)
        vk_session = vk_api.VkApi(
            token=TOKEN)
        vk = vk_session.get_api()
        vk.messages.send(user_id=int(event.obj.message['from_id']),
                         message=f'{data.today().date()} {data.time()} МСК {days[str(data.today().weekday())]}',
                         random_id=random.randint(0, 2 ** 64))
    else:
        vk_session = vk_api.VkApi(
            token=TOKEN)
        vk = vk_session.get_api()
        vk.messages.send(user_id=int(event.obj.message['from_id']),
                         message=f'У нас есть возможность узнать время',
                         random_id=random.randint(0, 2 ** 64),)


if __name__ == '__main__':
    main()
