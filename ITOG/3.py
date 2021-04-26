import requests
from flask import jsonify


def hippocampus(host, port, **kwargs):
    data = requests.get(f'http://{host}:{port}').json()
    print(data)
    print(kwargs['color'])
    flag = False
    d = dict()
    for di in data:
        if list(kwargs.keys()) == list(di.keys()):
            print('true')
            flag = True
            d = di
            break
    if flag:
        for key in d.keys():
            d[key].append(kwargs[key])
    else:
        d = dict()
        for key in kwargs.keys():
            d[key] = []
            d[key].append(kwargs[key])
        data.append(d)
    print(data)
    return jsonify(data)


hippocampus(host='127.0.0.1', port=8080, color='orange', size='medium', danger=15)
