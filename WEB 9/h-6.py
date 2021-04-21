from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from data import db_session
from data.user import User
from data.jobs import Jobs


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeatpassword = PasswordField('Повторите пароль', validators=[DataRequired()])

    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])

    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_session.global_init("db/mars.db")
        # db_session.global_init(name)
        db_sess = db_session.create_session()

        print(form.surname.data, form.name.data, form.address.data)

        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.address = form.address.data
        user.age = int(form.age.data)
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.hashed_password = form.password.data
        user.email = form.username.data
        db_sess.add(user)
        db_sess.commit()

        return redirect('/success')
    return render_template('form.html', title='Авторизация', form=form)

@app.route('/success')
def do():
    return f'Регистрация удалась'



if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)