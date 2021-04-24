from data import db_session
from flask import Flask, render_template, redirect, request, abort, jsonify
from data.user import User
from data.jobs import Jobs
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from forms.jobs_form import JobsForm
from forms.login import LoginForm
from forms.registr import RegistrForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob',  methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.team_leader = form.team_leader.data
        jobs.job = form.job.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data


        current_user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('addjob.html', title='Добавление работы',
                           form=form)


@app.route('/register', methods=['GET', 'POST'])
def add_user():
    form = RegistrForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        user = User()
        user.email = form.email.data
        user.set_password(form.password.data)
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        db_sess.add(user)
        login_user(user)
        db_sess.commit()
        return redirect('/')
    return render_template('registration.html', title='Добавление пользователя',
                           form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def do():
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


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        return f'{jobs.name}'
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished

        else:
            abort(400, {'message': 'custom error message to appear in body'})

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('addjob.html', form=form)


def main():
    db_session.global_init("db/mars.db")
    # db_session.global_init(name)
    db_sess = db_session.create_session()


if __name__ == '__main__':
    main()
    app.run(host='localhost', port=8080, debug=True)