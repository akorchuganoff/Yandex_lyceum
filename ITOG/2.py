import csv

with open('secret_law.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=':', quotechar='"')
    d = dict()
    for elem in reader:
        if int(elem['danger']) > 5:
            di = dict()
            di["date"] = elem["date"]
            di["place"] = elem["place"]
            di["danger"] = elem["danger"]

            d[elem['creature']] = di
    print(d)