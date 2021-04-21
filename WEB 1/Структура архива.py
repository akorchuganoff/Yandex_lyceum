from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    print(myzip.namelist())
    # for name in myzip.namelist():
    #     print(str(name))
        # f = ''
        # c = name.count('/')
        # if name[-1] == '/':
        #     c -= 1
        #     f += '  ' * c
        #     a = name.split('/')
        #     f += a[-2]
        # else:
        #     f += '  ' * c
        #     a = name.split('/')
        #     f += a[-1]
        # print(f)