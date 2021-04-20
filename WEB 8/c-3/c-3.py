from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/list_prof/<type>')
def do(type):
    prof = ['Аудитор', 'Аналитик', 'Банкир', 'Брокер', 'Бухгалтер', 'Маркетолог','Менеджер по работе с клиентами', 'Налоговый инспектор']
    return render_template('list_prof.html', type=type, prof=prof)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)