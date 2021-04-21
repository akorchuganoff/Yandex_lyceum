import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg", nargs='*', type=str)
args = parser.parse_args()

if len(args.arg) <= 0:
    print('NO PARAMS')
elif len(args.arg) == 1:
    print('TOO FEW PARAMS')
elif len(args.arg) >= 3:
    print('TOO MANY PARAMS')
else:
    try:
        print(int(args.arg[0]) + int(args.arg[1]))
    except Exception as e:
        print(e.__class__.__name__)