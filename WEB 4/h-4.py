import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
parser.add_argument('arg', type=str, nargs='*')

args = parser.parse_args()

d = {}
for i in range(len(args.arg)):
    k, v = args.arg[i].split('=')
    d[k] = v

data = list(d.items())
if args.sort:
    data.sort(key=lambda par: par[0])

for elem in data:
    print(f'Key: {elem[0]} Value: {elem[1]}')