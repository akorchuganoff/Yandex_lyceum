from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('ID астронавта', validators=[DataRequired()])
    userpass = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_name = StringField('ID капитана', validators=[DataRequired()])
    cap_pass = PasswordField('Пароль капитана', validators=[DataRequired()])

    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)