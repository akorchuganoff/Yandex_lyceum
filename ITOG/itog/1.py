import sys


def do(line):
    last_line = line[:-1]
    first = last_line.replace('AX', 'B')
    second = first.replace('BXX', 'C')
    new_line = second.replace("CXXX", "A")
    while last_line != new_line:
        last_line = new_line
        first = last_line.replace('AX', 'B')
        second = first.replace('BXX', 'C')
        new_line = second.replace("CXXX", "A")
    return new_line


if __name__ == '__main__':
    for line in sys.stdin:
        print(do(line))
