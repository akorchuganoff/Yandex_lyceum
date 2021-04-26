import csv
import argparse
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/fairy/')
def fairy():
    global args

    with open('muddy.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=':', quotechar='"')
        print(reader)

def do():
    with open('muddy.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=':', quotechar='"')
        print(reader)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--server', type=str, required=True, dest='host')
    # parser.add_argument('--port', type=int, required=True, dest='port')
    # parser.add_argument('--filename', type=str, required=True, dest='filename')
    # args = parser.parse_args()
    # app.run(host='127.0.0.1', port=8080, debug=True)
    do()
# cd /d D:\projects\ITOG\itog