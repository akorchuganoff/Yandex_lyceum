import os


def human_read_format(size):
    count = 0
    n = size
    while n >= 1024:
        n //= 1024
        count += 1
    if count == 0:
        return f'{size}Б'
    if count == 1:
        return f'{round(size/1024)}КБ'
    if count == 2:
        return f'{round(size/(1024**2))}МБ'
    if count == 3:
        return f'{round(size/(1024**3))}ГБ'


def get_files_sizes():
    n = []
    for i in os.listdir():
        if os.path.isfile(i):
            n.append(f'{i} {human_read_format(os.path.getsize(i))}')
    return '\n'.join(n)
