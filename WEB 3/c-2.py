import datetime
import schedule

i = 1

def job():
    print('Ку' * (datetime.datetime.now().hour % 12))

schedule.every().hour.at(':00').do(job)
while True:
    schedule.run_pending()