# import argparse
#
#
# def count_lines(path):
#     try:
#         with open(path, 'r') as file:
#             data = file.readlines()
#         flag = len(data)
#     except Exception:
#         flag = 0
#     return flag
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--file", type=str)
#     args = parser.parse_args()
#     print(count_lines(args.file))

from d_3 import format_text_block

format_text_block(20, 30, 'in.txt')