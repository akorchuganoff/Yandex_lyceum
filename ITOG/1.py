import sys


def count_lines(line):
    last = line[0]
    count_max = 1
    count = 1
    for i in range(1, len(line)):
        if line[i] != last:
            count += 1
            last = line[i]
        else:
            if count > count_max:
                count_max = count
            count = 1

    if count > count_max:
        count_max = count
    return count_max


if __name__ == '__main__':
    for line in sys.stdin:
        print(count_lines(line))