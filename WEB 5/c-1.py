import requests
import json

host = input()
port = input()
a = int(input())
b = int(input())

http = f'http://{host}:{port}?a={a}&b={b}'
# http = f'http://{host}:{port}'
r = requests.get(http).json()

arr = r['result']
arr.sort(key=lambda x: int(x))
print(*arr)
print(r['check'])
