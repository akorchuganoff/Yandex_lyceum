from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def photo():
    global fname
    if request.method == 'GET':
        return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Результаты</title></head>
<body>
<div>
    <form class="login_form" method="post" enctype="multipart/form-data">
        <div class="form-group"><label for="photo">Приложите фотографию</label> <input type="file"
                                                                                       class="form-control-file"
                                                                                       id="photo" name="file"></div>
        <div><img src="{url_for('static', filename=f'img/{fname}')}" width=400px></div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</div>
</body>
</html>'''
    elif request.method == 'POST':
        print(request.files)
        img = request.files['file']
        fname = img.filename
        img.save(f"static/img/{fname}")
        return 'форма отправлена'


if __name__ == '__main__':
    fname = ''
    app.run(host='localhost', port=8080, debug=True)
