from requests import post, get, delete

print(get('http://localhost:5000/api/v2/users').json())
# get all users

print(post('http://localhost:5000/api/v2/users').json())
# empty request

print(post('http://localhost:5000/api/v2/users',
           json={'name': 'Николай петрович'}).json())
# only name of user

print(post('http://localhost:5000/api/v2/users',
           json={'id': 5,
                 'surname': 'Иванов',
                 'name': 'Иван',
                 'age': 10,
                 'position': 'Студент',
                 'speciality': 'Инженер',
                 'address': 'module_5',
                 'email': 'ii@mars.org',
                 'city_from': 'Барнаул'}).json())
# id already exist

print(post('http://localhost:5000/api/v2/users',
           json={'id': 7,
                 'surname': 'Иванов',
                 'name': 'Иван',
                 'age': 10,
                 'position': 'Студент',
                 'speciality': 'Инженер',
                 'address': 'module_5',
                 'email': 'scott_chief@mars.org',
                 'city_from': 'Барнаул'}).json())
# email already exist

print(post('http://localhost:5000/api/v2/users',
           json={'id': 6,
                 'surname': 'Иванов',
                 'name': 'Иван',
                 'age': 10,
                 'position': 'Студент',
                 'speciality': 'Инженер',
                 'address': 'module_5',
                 'email': 'ii@mars.org',
                 'city_from': 'Барнаул'}).json())
# correct request? user with 6 id created

print(get('http://localhost:5000/api/v2/users/6').json())
# check user with 6 id

print(delete('http://localhost:5000/api/v2/users/23456734').json())
# delete user with id 6

print(delete('http://localhost:5000/api/v2/users/6').json())
# there is not user with id 6

print(get('http://localhost:5000/api/v2/users').json())
# all users
