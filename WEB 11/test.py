import requests

# print(requests.get('http://127.0.0.1:8080/api/jobs').json())
# print(requests.post('http://127.0.0.1:8080/api/jobs', json={'collaborators': '1, 2', 'is_finished': False, 'job': 'print(input())', 'id': 4, 'work_size': 10, 'team_leader': 1}).json()) # коректный запрос
print(requests.get('http://127.0.0.1:8080/api/jobs').json())
print(requests.put('http://127.0.0.1:8080/api/jobs/1', json={'is_finished': True}).json())
print(requests.put('http://127.0.0.1:8080/api/jobs/1', json={'strange': True}).json())# нет такого поля
print(requests.put('http://127.0.0.1:8080/api/jobs/1', json={'is_finished': 'True'}).json())# не того типа
# print(requests.delete('http://127.0.0.1:8080/api/jobs/5').json())
# print(requests.delete('http://127.0.0.1:8080/api/jobs/6').json())
# print(requests.delete('http://127.0.0.1:8080/api/jobs/7').json())
print(requests.get('http://127.0.0.1:8080/api/jobs').json())
# print(requests.post('http://127.0.0.1:8080/api/jobs', json={'collaborators': '1, 2', 'is_finished': False, 'job': 'print(input())', 'id': 5, 'work_size': 10, 'team_leader': 1}).json()) # коректный запрос
# print(requests.post('http://127.0.0.1:8080/api/jobs', json={'collaborators': '1, 2', 'job': 'print(input())', 'id': 5, 'work_size': 10, 'team_leader': 1}).json()) # нет поля "is_finished"
# print(requests.post('http://127.0.0.1:8080/api/jobs', json={'collaborators': '1, 2', 'is_finished': False, 'id': 4, 'work_size': 10, 'team_leader': 1}).json()) #нет поля 'job'
# print(requests.post('http://127.0.0.1:8080/api/jobs', json={'collaborators': '1, 2', 'is_finished': False, 'job': 'print(input())', 'work_size': 10, 'team_leader': 1}).json()) # нет поля 'id"
