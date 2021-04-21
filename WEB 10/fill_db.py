from data import db_session
from data.user import User
db_session.global_init("db/mars.db")
db_sess = db_session.create_session()

user = User()
user.surname = 'qwerty'
user.name = 'qwerty'
user.age = 12
user.position = 'chief'
user.speciality = 'qwerty'
user.email = 'qwert@mail.ru'
user.set_password('12345678')
user.address = 'module_1'
db_sess.add(user)
db_sess.commit()