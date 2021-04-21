import shutil
import datetime


def make_reserve_arc(source, dest):
    shutil.make_archive(str(datetime.datetime.now()), 'zip', root_dir=source, base_dir=dest)


print('Введите путь к директории')
source = input()
print('Введите путь к папке назначения через пробел')
dest = input()
make_reserve_arc(source, dest)