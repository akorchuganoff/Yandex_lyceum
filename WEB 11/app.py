from flask import Flask
import c_1

app = Flask(__name__)
app.register_blueprint(c_1.blueprint)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')