from data import db_session
from flask import Flask, render_template
from data.user import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def do():
    db_session.global_init("db/mars.db")
    # db_session.global_init(name)
    db_sess = db_session.create_session()

    jobs = db_sess.query(Jobs).all()
    arr = []
    for job in jobs:
        d_job = job.to_dict(only=('job', 'team_leader', 'work_size', 'collaborators', 'is_finished'))
        ident = d_job['team_leader']
        user = db_sess.query(User).filter(User.id == ident).first()
        d_job['team_leader'] = user.name + user.surname
        arr.append(d_job)

    return render_template('c-7.html', arr=arr)


def main():
    db_session.global_init("db/mars.db")
    # db_session.global_init(name)
    db_sess = db_session.create_session()

    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'make cake'
    # job.work_size = 2
    # job.collaborators = '2, 4'
    # job.is_finished = False
    # db_sess.add(job)
    # db_sess.commit()


if __name__ == '__main__':
    main()
    # app.run(host='localhost', port=8080, debug=True)