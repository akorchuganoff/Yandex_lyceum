import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("file", type=str)
args = parser.parse_args()
try:
    with open(args.file, 'r') as file:
        data = file.readlines()
except Exception as e:
    print("ERROR")

data[-1] += '\n'

if args.sort:
    data.sort()
for i in range(len(data)):
    if args.num:
        print(f'{i} {data[i]}', end='')
    else:
        print(data[i], end='')

if args.count:
    print(f'rows count: {len(data)}')