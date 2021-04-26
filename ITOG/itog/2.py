import csv
import json

with open('trouble.json', mode='r') as jsonfile:
    data = json.load(jsonfile)

rows = []
for di in data:
    if di['self'] != di['advice']:
        row = [di['name'], di['habitat'], di['self'], di['advice']]
        rows.append(row)

rows.sort(key=lambda row: row[0])

biglist = [['name', 'habitat', 'self', 'advice']]
for elem in rows:
    biglist.append(elem)

with open('advices.csv', mode='w') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=',', quotechar='"')
    writer.writerows(biglist)