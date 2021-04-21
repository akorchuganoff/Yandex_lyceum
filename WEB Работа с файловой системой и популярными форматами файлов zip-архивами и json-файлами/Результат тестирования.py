import json
import sys

with open('cats_json.json') as cat_file:
    data = json.load(cat_file)

tests = []
for key, value in data.items():
    for elem in value:
        a = []
        for k, v in elem.items():
            if k == 'required_tests' or k == 'points':
                a.append((k, v))
        tests.append(a)

print(tests)

count = 0
result = 0
for line in sys.stdin:
    count += 1
    if line == 'ok\n':
        print(count)
        for elem in tests:
            print(elem)
            if count in list(elem[0][1]):
                result += elem[1][1] / len(elem[0][1])
                break
print(result)