import json
import sys

with open('scoring.json') as jsonfile:
    data = json.load(jsonfile)

# print(type(data))
# for key, value in data.items():
#     for elem in value:
#         print(elem)
#         for k, v in elem.items():
#             if type(v) == list:
#                 for i in range(len(v)):
#                     v[i] = str(v[i])
#                 print(f'{k}: {", ".join(v)}')
#             else:
#                 print(f'{k}: {v}')
#         print()

count = 1
summ = 0
for line in sys.stdin:
    line = list(line)
    if line[0] == 'o' and line[1] == 'k':
        for key, value in data.items():
            for elem in value:
                if count in elem['required_tests']:
                    summ += elem['points'] / len(elem['required_tests'])
    else:
        pass
    count += 1
print(int(summ))