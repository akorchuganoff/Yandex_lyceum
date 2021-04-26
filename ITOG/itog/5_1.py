import csv
import argparse
import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/fairy/')
def fairy():
    return jsonify(d)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", dest="server", type=str)
    parser.add_argument("--port", dest="port", type=str)
    parser.add_argument("--filename", dest="filename", type=str)
    args = parser.parse_args()
    csvfile = open(args.filename, mode='r')
    reader = csv.DictReader(csvfile, delimiter=':', quotechar='"')

    d = {"fairy": [], "doxy": []}
    for elem in reader:
        if int(elem['presence of wool']) or int(elem['number of pair hands']) > 1 or \
                int(elem['number of pair legs']) > 1:
            d["doxy"].append([elem["color"], int(elem["size"])])
        else:
            d["fairy"].append([elem["color"], int(elem["size"])])
    d["fairy"].sort(key=lambda x: (x[0], x[1]))
    d["doxy"].sort(key=lambda x: (x[0], x[1]))

    app.run(host=args.server, port=args.port)
