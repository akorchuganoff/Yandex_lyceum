import vk_api
import datetime


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
    response = vk.photos.get(album_id='wall', owner_id=-204212860)
    if response['items']:
        for i in response['items']:
            for j in range(len(i['sizes'])):
                # print(i['sizes'][j]['height'])
                print(f"heigth: {i['sizes'][j]['height']} width: {i['sizes'][j]['width']} url: {i['sizes'][j]['url']}")
    # if response['items']:
    #     for i in response['items']:
    #         print(f"{i['text']}")
    #         print(datetime.datetime.utcfromtimestamp(i['date']).strftime('date: {%Y-%m-%d}, time: {%H:%M:%S}'))


if __name__ == '__main__':
    main()