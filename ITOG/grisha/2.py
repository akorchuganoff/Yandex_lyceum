import csv
import json

with open('stealth.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')

    d = dict()
    d['size'] = []
    d['habitat'] = []
    d['magic'] = []
    d['fast'] = []
    d['other'] = []

    for elem in reader:
        if elem['size'] == '1':
            d['size'].append(elem['creature'])
        if elem['habitat'] == '1':
            d['habitat'].append(elem['creature'])
        if elem['magic'] == '1':
            d['magic'].append(elem['creature'])
        if elem['fast'] == '1':
            d['fast'].append(elem['creature'])
        if elem['other'] == '1':
            d['other'].append(elem['creature'])

    for key in d.keys():
        d[key].sort()

with open('hidden.json', mode='w') as file:
    json.dump(d, file, ensure_ascii=False)
