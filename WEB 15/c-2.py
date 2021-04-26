import vk_api
import datetime

LOGIN, PASSWORD = 'login', 'password'
LOGIN = '89021419881'
PASSWORD = '2111Efiop'


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.friends.get(fields=['nickname', 'bdate'])
    friend_list = []
    if response['items']:
        for i in response['items']:
            if 'bdate' in i.keys():
                friend_list.append((i['first_name'], i['last_name'], i['bdate']))
            else:
                friend_list.append((i['first_name'], i['last_name'], 'Дата рождения не указана'))
    friend_list.sort(key=lambda friend: friend[1])
    for elem in friend_list:
        print(*elem)

if __name__ == '__main__':
    main()