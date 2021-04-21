from data import db_session
from flask import Flask, render_template
from data.user import User
from data.jobs import Jobs


def main(name):
    # db_session.global_init("db/mars.db")
    db_session.global_init(name)
    db_sess = db_session.create_session()

    for user in db_sess.query(User).filter(User.age < 21, User.address == 'module_1').all():
        user.address = 'module_3'
    db_sess.commit()


if __name__ == '__main__':
    main(input())