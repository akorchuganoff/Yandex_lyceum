from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promoution():
    promo = ['Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!']

    return '</br>'.join(promo)

@app.route('/image_mars')
def image():
    return """<!DOCTYPE html>
                <html>
                 <head>
                  <meta charset="utf-8">
                  <title>Привет, Марс!</title>
                 </head>
                 <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/riana.jpg')}" 
                     alt="здесь должна была быть картинка, но не нашлась">
                  <h1>Вот она, красная планета</h1>
                 </body>
                </html>"""

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
