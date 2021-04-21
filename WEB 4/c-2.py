# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("--barbie", type=int, default=50)
# parser.add_argument("--cars", type=int, default=50)
# parser.add_argument("--movie", choices={"melodrama", "football", "other"}, default="other")
#
# args = parser.parse_args()
# if args.barbie > 100 or args.barbie < 0:
#     args.barbie = 50
# if args.cars > 100 or args.cars < 0:
#     args.cars = 50
#
# if args.movie == "melodrama":
#     args.movie = 0
# elif args.movie == "football":
#     args.movie = 100
# elif args.movie == "other":
#     args.movie = 50
#
# boy = (100 - args.barbie + args.cars + args.movie) / 3
# girl = 100 - int(boy)
#
# print(f'boy: {int(boy)}')
# print(f'girl: {girl}')

from get_lines import count_lines

print(count_lines('unknown_file.txt'))