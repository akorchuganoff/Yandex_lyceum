from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def do():
    return jsonify({
        "color": "brown",
        "weight": 50,
        "size": "small"
    })


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
