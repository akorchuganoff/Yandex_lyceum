from data import db_session
from flask import Flask
from data.user import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    cap = User()
    cap.surname = 'Scott'
    cap.name = 'Ridley'
    cap.age = 21
    cap.position = 'captain'
    cap.speciality = 'research engineer'
    cap.address = 'module_1'
    cap.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(cap)

    user1 = User()
    user1.surname = 'Black'
    user1.name = 'Adam'
    user1.age = 19
    user1.position = 'user'
    user1.speciality = 'doctor'
    user1.address = 'module_3'
    user1.email = 'Adam_Black@mars.org'
    db_sess.add(user1)

    user2 = User()
    user2.surname = 'Green'
    user2.name = 'Jereme'
    user2.age = 25
    user2.position = 'user'
    user2.speciality = 'scientist'
    user2.address = 'module_1'
    user2.email = 'Green_Jereme@mars.org'
    db_sess.add(user2)

    user3 = User()
    user3.surname = 'Braun'
    user3.name = 'Simon'
    user3.age = 22
    user3.position = 'user'
    user3.speciality = 'cooker'
    user3.address = 'module_2'
    user3.email = 'Simon_Braun@mars.org'
    db_sess.add(user3)
    db_sess.commit()


if __name__ == '__main__':
    main()
