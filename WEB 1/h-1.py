from zipfile import ZipFile


def transform(x):
    d = {0: 'Б', 1: 'КБ', 2: 'МБ', 3: 'ГБ'}
    c = 0
    while x // 1024 >= 1:
        x //= 1024
        c += 1
    return str(x) + d[c]


with ZipFile('input.zip', mode='r') as myzip:
    # print(myzip.namelist())
    for name in myzip.namelist():
        f = ''
        c = name.count('/')
        if name[-1] == '/':
            c -= 1
            f += '  ' * c
            a = name.split('/')
            f += a[-2]
        else:
            f += '  ' * c
            a = name.split('/')
            f += a[-1] + ' ' + transform(myzip.getinfo(name).file_size)
        print(f)