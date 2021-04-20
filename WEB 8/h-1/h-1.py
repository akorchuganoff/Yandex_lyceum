from flask import Flask, render_template, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    L = ['sljfvk', 'skdjfnm', 'sdf;jn', 'fdgljsgf', 'slfjn']
    return render_template('distribution.html', list=L)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)