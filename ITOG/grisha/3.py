import requests


def billywig(server, port, **kwargs):
    data = requests.get(f'http://{server}:{port}').json()
    d = data[kwargs['creature']]
    for key in kwargs.keys():
        if key == 'creature':
            continue
        if key in d.keys():
            d[key].append(kwargs[key])
        else:
            d[key] = [kwargs[key]]
    return data
