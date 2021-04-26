import vk_api
from vk_api import VkUpload
import datetime

LOGIN, PASSWORD = 'login', 'password'




def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(['static/img/adult.png'], group_id=204212860)

    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, vk_photo_id, sep="\n")

    vk = vk_session.get_api()
    vk.wall.post(owner_id=-204212860, message="Test", attachments=[vk_photo_id], from_group=1)


if __name__ == '__main__':
    main()