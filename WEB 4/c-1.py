import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg", type=str, nargs="*")

args = parser.parse_args()
if len(args.arg) > 0:
    for i in range(len(args.arg)):
        print(args.arg[i])
else:
    print("no args")