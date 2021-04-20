from flask import Flask, url_for

app = Flask(__name__)

@app.route('/choice/<planet_name>')
def do(planet_name):
    return f'''<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
        <title>Пример формы</title>
    </head>
    <body>
        <h1>Мое предложение: {planet_name}</h1>
        <h2> Эта планета близка к земле</h2>
        <div>
            <label class="alert alert-primary" role="alert">На ней много необходимых ресурсов</label>
        </div>
        <div>
            <label class="alert alert-primary" role="alert">На ней есть вода и атмосфера</label>
        </div>
        <div>
            <label class="alert alert-primary" role="alert">На ней есть небольшое магнитное поле</label>
        </div>
        <div>
            <label class="alert alert-primary" role="alert">Наконец она просто красива</label>
        </div>
    </body>
</html>'''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)