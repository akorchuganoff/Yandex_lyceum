from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/index/<title>')
def do(title):
    print(title)
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)