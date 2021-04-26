import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

TOKEN = '58883f4c0d6d57119e3ebb47633b5c573f4643363613ec4b65983c8cee6fe9dfb7e0e74389eeff5d811da'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 204212860)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            send_message(event)


def send_message(event):
    user_id = event.obj.message['from_id']
    vk_session = vk_api.VkApi(
        token=TOKEN)
    vk = vk_session.get_api()
    response = vk.users.get(user_ids=user_id, fields=['city', 'nickname'])
    if response:
        for i in response:
            print(i)
            vk.messages.send(user_id=event.obj.message['from_id'], message=f"Привет {i['first_name']}!",
                             random_id=random.randint(0, 2 ** 64))
            if 'city' in i.keys():
                vk.messages.send(user_id=event.obj.message['from_id'], message=f"Как поживает {i['city']['title']}?",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
