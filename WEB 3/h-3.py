import datetime
import schedule

diapason = input().split('-')
if diapason[0][0] == '0':
    beg = int(diapason[0][1])
else:
    beg = int(diapason[0])

if diapason[1][0] == '0':
    end = int(diapason[1][1])
else:
    end = int(diapason[1])

ne_budi_time = [i for i in range(beg, end+1)]

def job():
    hour = datetime.datetime.now().hour
    if hour in ne_budi_time:
        return
    print('Ку' * (hour % 12))

schedule.every().hour.at(':00').do(job)
while True:
    schedule.run_pending()