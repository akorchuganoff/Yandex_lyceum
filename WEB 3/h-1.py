import sys

d = {}
flag = 0
for i in range(1, len(sys.argv)):
    if sys.argv[i] == '--sort':
        flag = 1
        continue
    k, v = sys.argv[i].split('=')
    d[str(k)] = str(v)

data = list(d.items())
if flag == 1:
    data.sort(key=lambda par: par[0])

for elem in data:
    k, v = elem[0], elem[1]
    print(f'Key: {k} Value: {v}')