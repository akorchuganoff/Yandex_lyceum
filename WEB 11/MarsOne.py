from flask import Flask, render_template, redirect, request, abort
from data import db_session
from data.colonists import User
from data.jobs import Jobs
from data.departments import Department
from data.category import Category
from forms.colonist import RegisterForm, LoginForm
from forms.jobs import JobsForm
from forms.departments import DepartmentForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import datetime
import c_1

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.register_blueprint(c_1.blueprint)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
def index():
    team_leaders = list()
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    for job in jobs:
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        team_leaders.append(f'{user.surname} {user.name}')
    return render_template("list_of_tables.html", title='Work log', jobs=jobs, team_leaders=team_leaders)


@app.route("/departments_tables")
def departments_tables():
    departments_leaders = list()
    db_sess = db_session.create_session()
    departments = db_sess.query(Department).all()
    for department in departments:
        user = db_sess.query(User).filter(User.id == department.chief).first()
        departments_leaders.append(f'{user.surname} {user.name}')
    return render_template("list_of_departments.html", title='List of departments',
                           departments=departments, departments_leaders=departments_leaders)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="User already exists")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            position=form.position.data,
            speciality=form.speciality.data,
            age=form.age.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Registration', form=form)


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
                               message="Wrong login or password",
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.job = form.title.data
        job.team_leader = form.team_leader.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        category = db_sess.query(Category).filter(form.category.data == Category.id).first()
        job.categories.append(category)
        job.is_finished = form.is_finished.data
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Adding a job',
                           form=form)


@app.route('/departments',  methods=['GET', 'POST'])
@login_required
def add_departments():
    form = DepartmentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = Department()
        department.chief = form.chief.data
        department.title = form.title.data
        department.email = form.email.data
        department.members = form.members.data
        db_sess.add(department)
        db_sess.commit()
        return redirect('/departments_tables')
    return render_template('departments.html', title='Adding a department',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         ((Jobs.user == current_user) | (current_user.id == 1))
                                          ).first()
        if job:
            form.team_leader.data = job.team_leader
            form.title.data = job.job
            form.collaborators.data = job.collaborators
            form.work_size.data = job.work_size
            form.is_finished.data = job.is_finished
            form.category.data = job.categories[0].id
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         ((Jobs.user == current_user) | (current_user.id == 1))
                                         ).first()
        if job:
            job.team_leader = form.team_leader.data
            job.job = form.title.data
            job.collaborators = form.collaborators.data
            job.work_size = form.work_size.data
            for category in db_sess.query(Category).all():
                try:
                    job.categories.remove(category)
                except Exception:
                    pass
            category = db_sess.query(Category).filter(form.category.data == Category.id).first()
            job.categories.append(category)
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Edit job',
                           form=form
                           )


@app.route('/departments/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departments(id):
    form = DepartmentForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == id,
                                                      ((Department.user == current_user) |
                                                       (current_user.id == 1))
                                                      ).first()
        if department:
            form.chief.data = department.chief
            form.title.data = department.title
            form.email.data = department.email
            form.members.data = department.members
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == id,
                                                      ((Department.user == current_user) |
                                                       (current_user.id == 1))
                                                      ).first()
        if department:
            department.chief = form.chief.data
            department.title = form.title.data
            department.email = form.email.data
            department.members = form.members.data
            db_sess.commit()
            return redirect('/departments_tables')
        else:
            abort(404)
    return render_template('departments.html',
                           title='Edit department',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id,
                                     ((Jobs.user == current_user) | (current_user.id == 1))
                                     ).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departments_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def departments_delete(id):
    db_sess = db_session.create_session()
    department = db_sess.query(Department).filter(Department.id == id,
                                                  ((Department.user == current_user) |
                                                   (current_user.id == 1))
                                                  ).first()
    if department:
        db_sess.delete(department)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments_tables')


def main():
    db_session.global_init("db/colonists.db")
    app.run(host='localhost', port=8080,debug=True)


if __name__ == '__main__':
    main()