from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/training/<prof>')
def do(prof):
    print(prof)
    return render_template('training.html', specialitet=prof)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)