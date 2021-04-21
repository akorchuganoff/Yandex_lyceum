import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', metavar='PER_DAY', type=str, dest='day')
parser.add_argument('--per-week', metavar='PER_WEEK', type=int, dest='week')
parser.add_argument('--per-month', metavar='PER_MONTH', type=int, dest='month')
parser.add_argument('--per-year', metavar='PER_YEAR', type=int, dest='year')
parser.add_argument('--get-by', type=str, choices=['day', 'month', 'year'],
                    dest='get', default='day')

args = parser.parse_args()

summ = 0

if args.day:
    summ += int(args.day)
if args.week:
    summ += args.week / 7
if args.month:
    summ += args.month / 30
if args.year:
    summ += args.year / 360


if args.get == 'day':
    print(int(summ))
elif args.get == 'month':
    print(int(summ * 30))
elif args.get == 'year':
    print(int(summ * 360))