import sys

count = 0
num = 0
sort = 0

name = ''

for elem in range(1, len(sys.argv)):
    if sys.argv[elem] == '--count':
        count = 1
    elif sys.argv[elem] == '--num':
        num = 1
    elif sys.argv[elem] == '--sort':
        sort = 1
    else:
        name = sys.argv[elem]

try:
    with open(name, mode='r') as file:
        data = file.readlines()

except Exception:
    # print(e.__class__.__name__)
    print('ERROR')
    sys.exit(1)


if sort == 1:
    data.sort()

if num:
    for i in range(len(data)):
        if data[i][-1] == '\n':
            print(f'{i} {data[i][:-1]}')
        else:
            print(f'{i} {data[i]}')
    if count == 1:
        print(f'rows count: {len(data)}')

else:
    for i in range(len(data)):
        if data[i][-1] == '\n':
            print(f'{data[i][:-1]}')
        else:
            print(f'{data[i]}')
    if count == 1:
        print(f'rows count: {len(data)}')