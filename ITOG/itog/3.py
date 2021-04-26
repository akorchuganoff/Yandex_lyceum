import requests


# import json


def hippogriff(port, host, **kwargs):
    data = requests.get(f'http://{host}:{port}').json()
    for key in kwargs.keys():
        if key in data.keys():
            value = data[key]
            data[key] = max(value, kwargs[key])
        else:
            data[key] = kwargs[key]
    return data

# print(hippogriff(8080, '127.0.0.1', magic='high', weight=15, color='dappled'))
