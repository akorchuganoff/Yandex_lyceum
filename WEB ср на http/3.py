import argparse
import requests
import csv


def make_stats(d, mult, digits):
    data_list = list(d.items())
    data_list.sort(key=lambda par: par[1], reverse=True)
    row = []
    for i in range(len(data_list)):
        if data_list[i][1] % 2 == 1 and len(str(data_list[i][1])) == digits:
            row.append(str(data_list[i][0]))
            row.append(str(data_list[i][1]))
            break
    for i in range(len(data_list) - 1, -1, -1):
        if data_list[i][1] % mult == 0 and len(str(data_list[i][1])) == digits:
            row.append(str(data_list[i][0]))
            row.append(str(data_list[i][1]))
            break
    m = 1
    for i in range(len(data_list)):
        if len(str(data_list[i][1])) == digits:
            m *= data_list[i][1]
    row.append(m % (mult + 1))
    return row


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("value", type=str)
    parser.add_argument("--digits", type=int, default=1, dest='digits')
    parser.add_argument("--mult ", type=int, default=1, dest='mult')
    arg = parser.parse_args()
    response = requests.get(f'http://{arg.host}:{arg.port}').json()
    response_key = response[f'{arg.value}']

    print(response_key)
    rows = []
    for d in response_key:
        rows.append(make_stats(d, mult=arg.mult, digits=arg.digits))

    with open('gravity.csv', mode='w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"')
        writer.writerows(rows)
