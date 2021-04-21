def main():
    global_init(input())
    db_sess = create_session()
    department = db_sess.query(Department).first()
    for user in db_sess.query(User).all():
        if str(user.id) in department.members.split(', '):
        print(user.surname, user.name)


if __name__ == '__main__':
    main()