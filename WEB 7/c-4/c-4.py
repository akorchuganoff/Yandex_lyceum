from flask import Flask, url_for

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
    return f'''<!DOCTYPE html>
                <html>
                 <head>
                  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  <title>Привет, Марс!</title>
                 </head>
                 <body>
                  <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/mars.jpg')}"
                     alt="здесь должна была быть картинка, но не нашлась">
                  <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства
                  </div>
                  <div class="alert alert-primary" role="alert">
                      Человечеству мала одна планета.
                  </div>
                  <div class="alert alert-primary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                  </div>
                  <div class="alert alert-primary" role="alert">
                      И начнем с Марса!
                  </div>
                  <div class="alert alert-primary" role="alert">
                      Присоединяйся!
                  </div>
                 </body>
                </html>'''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
