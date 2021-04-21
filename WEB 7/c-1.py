from flask import Flask, url_for, request

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

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def select():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пример формы</title>
                      </head>
                      <body>
                        <h1>Анкета претендента</h1>
                        <h2>на участие в миссии</h2>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                <div class="form-group">
                                    <label for="classSelect">Какое у вас образование?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>начальное</option>
                                      <option>среднее</option>
                                      <option>высшее</option>
                                    </select>
                                 </div>
                                <div>
                                    <label>Какие у вас есть профессии?</label>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept1" name="accept1">
                                    <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept2" name="accept2">
                                    <label class="form-check-label" for="acceptRules">пилот</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept3" name="accept3">
                                    <label class="form-check-label" for="acceptRules">строитель</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept4" name="accept4">
                                    <label class="form-check-label" for="acceptRules">врач</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept5" name="accept5">
                                    <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept6" name="accept6">
                                    <label class="form-check-label" for="acceptRules">климатолог</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept7" name="accept7">
                                    <label class="form-check-label" for="acceptRules">специалист по радиационной защите</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept8" name="accept8">
                                    <label class="form-check-label" for="acceptRules">астрогеолог</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept9" name="accept9">
                                    <label class="form-check-label" for="acceptRules">гляциолог</label>
                                </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="accept10" name="accept10">
                                    <label class="form-check-label" for="acceptRules">инженер жизнеобеспечения</label>
                                </div>
                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label for="about">Почему вы хотите принять участие в миссии</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Записаться</button>
                            </form>
                        </div>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
