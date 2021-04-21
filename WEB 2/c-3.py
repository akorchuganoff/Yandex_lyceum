import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

# Barnaul
geocode_request = f'http://geocode-maps.yandex.ru/1.x/?geocode=Барнаул&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]
    toponym_region = toponym["Components"][2]["name"]
    print(f"Барнаул: {toponym_region}")
else:
    print('request error')
    print(f'http code: {response.status_code} ({response.reason})')

# Мелеуз
geocode_request = f'http://geocode-maps.yandex.ru/1.x/?geocode=Мелеуз&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]
    toponym_region = toponym["Components"][2]["name"]
    print(f"Мелеуз: {toponym_region}")
else:
    print('request error')
    print(f'http code: {response.status_code} ({response.reason})')

# Йошкар-Ола
geocode_request = f'http://geocode-maps.yandex.ru/1.x/?geocode=Йошкар-Ола&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]
    toponym_region = toponym["Components"][2]["name"]
    print(f"Йошкар-Ола: {toponym_region}")
else:
    print('request error')
    print(f'http code: {response.status_code} ({response.reason})')