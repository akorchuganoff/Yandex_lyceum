import os


def transform(x):
    d = {0: 'Б', 1: 'КБ', 2: 'МБ', 3: 'ГБ'}
    c = 0
    while x // 1024 >= 1:
        x //= 1024
        c += 1
    return str(x) + d[c]


path = input()
os.chdir(path)
dirs = []
for elem in os.listdir():
    if os.path.isdir(elem):
        dirs.append(elem)
d = []
for elem in dirs:
    d.append((elem, os.path.getsize(elem)))
d.sort(key=lambda par: par[1], reverse=True)
for i in range(10):
    print(d[i][0], transform(d[i][1]), sep=' ' * (100 - len(d[i][0])))