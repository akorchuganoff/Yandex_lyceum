import argparse
import requests
import csv


def make_stats(key, values, not_mult, larger):
    values.sort()
    maxx = 0
    minn = 10 ** 9
    summ = 0
    count = 0

    for i in range(len(values)):
        if int(values[i]) % int(not_mult) != 0 and int(values[i]) > int(larger):
            if int(values[i]) > maxx:
                maxx = int(values[i])
            if int(values[i]) < minn:
                minn = int(values[i])
            summ += int(values[i])
            count += 1

    row = [key, maxx, minn, summ / count, summ]
    return row


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("--larger", type=int, default=1, dest='larger')
    parser.add_argument("--not_mult ", type=int, default=10, dest='not_mult')
    arg = parser.parse_args()
    response = requests.get(f'http://{arg.host}:{arg.port}').json()

    rows = []
    for k, v in response.items():
        rows.append(make_stats(k, v, not_mult=arg.not_mult, larger=arg.larger))

    rows.sort(key=lambda row: row[0])

    with open('heat.csv', mode='w') as csvfile:
        writer = csv.writer(csvfile, delimiter=':', quotechar='"')
        writer.writerows(rows)
