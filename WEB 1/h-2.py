import json
from zipfile import ZipFile

with ZipFile('input.zip', mode='r') as myzip:
    count = 0
    for name in myzip.namelist():
        if not myzip.getinfo(name).is_dir():
            if name[-5:] == '.json':
                with myzip.open(name, mode='r') as jsonfile:
                    data = json.load(jsonfile)
                for k, v in data.items():
                    if k == 'city' and v == 'Москва':
                        count += 1
    print(count)