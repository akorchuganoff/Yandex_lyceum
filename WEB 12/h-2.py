from requests import post, get, delete

print(get('http://localhost:5000/api/v2/jobs').json())
# All jobs

print(post('http://localhost:5000/api/v2/jobs').json())
# пустой запросempty request
print(post('http://localhost:5000/api/v2/jobs',
           json={'job': 'Писать письмо'}).json())
# only title

print(post('http://localhost:5000/api/v2/jobs',
           json={'id': 1,
                 'team_leader': 1,
                 'job': 'Писать письмо',
                 'work_size': 12,
                 'collaborators': '1, 2',
                 'categories': 2,
                 'is_finished': False}).json())
# Id already exist

print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 1,
                 'job': 'Писать письмо',
                 'work_size': 12,
                 'collaborators': '1, 2',
                 'categories': 1000,
                 'is_finished': False}).json())
# category didn't exist

print(post('http://localhost:5000/api/v2/jobs',
           json={'id': 4,
                 'team_leader': 1000,
                 'job': 'Писать письмо',
                 'work_size': 12,
                 'collaborators': '1, 2',
                 'categories': 2,
                 'is_finished': False}).json())
# user didn't exist

print(post('http://localhost:5000/api/v2/jobs',
           json={'id': 4,
                 'team_leader': 1,
                 'job': 'Писать письмо',
                 'work_size': 12,
                 'collaborators': '1, 2',
                 'categories': 2,
                 'is_finished': False}).json())
# correct request

print(get('http://localhost:5000/api/v2/jobs/4').json())
# check last request

print(delete('http://localhost:5000/api/v2/jobs/999').json())
# id didn't exist

print(delete('http://localhost:5000/api/v2/jobs/4').json())
# delete job

print(get('http://localhost:5000/api/v2/jobs').json())
# all jobs
