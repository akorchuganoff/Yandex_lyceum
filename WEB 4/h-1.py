import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--upper", action="store_true")
parser.add_argument("--lines", type=int, nargs='?')
parser.add_argument("input", type=str)
parser.add_argument("output", type=str)

args = parser.parse_args()
try:
    with open(args.input, 'r') as input_file:
        data = input_file.readlines()
except Exception:
    print(Exception.__class__.__name__)

if args.upper:
    for i in range(len(data)):
        data[i] = data[i].upper()

try:
    with open(args.output, 'w') as output_file:
        if args.lines:
            for i in range(min(args.lines, len(data))):
                output_file.write(data[i])
        else:
            for i in range(len(data)):
                output_file.write(data[i])
except Exception:
    print(Exception.__class__.__name__)