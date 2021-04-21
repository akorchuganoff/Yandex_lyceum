from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import IntegerField, EmailField


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')