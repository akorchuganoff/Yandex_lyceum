import sys


def solve(line):
    line = line[:-1]
    last = line[0]
    count = 1
    max_count = 1
    for i in range(1, len(line)):
        if line[i] != last:
            count += 1
            last = line[i]
        else:
            if max_count < count:
                max_count = count
            count = 1
            last = line[i]
    if max_count < count:
        max_count = count

    print(max_count)


if __name__ == '__main__':
    for line in sys.stdin:
        solve(line)
