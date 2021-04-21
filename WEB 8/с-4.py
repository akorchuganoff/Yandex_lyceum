from flask import Flask, request, url_for, render_template
app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def do():
    d = {'title': 'mars',
         'surname': 'Watny',
         'name': 'Mark',
         'education': 'выше среднего',
         'profession': 'штурман марсохода',
         'sex': 'male',
         'motivation': 'Всегда мечтал застрять на Марсе!',
         'ready': True}
    return render_template('auto_answer.html', d=d)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)