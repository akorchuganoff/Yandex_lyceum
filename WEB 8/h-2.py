from flask import Flask, render_template, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<sex>/<int:age>', methods=['GET', 'POST'])
def login(sex, age):
    return render_template('table.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)