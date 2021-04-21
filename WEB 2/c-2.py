import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

#Хабаровск
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Хабаровск&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]
    toponym_coords = toponym["Address"]["Components"][1]["name"]
    print(f'Хабаровск: {toponym_coords}')
else:
    print("request error")
    print(f'http code: {response.status_code} ({response.reason})')

# Уфа
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Уфа&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
        "GeocoderMetaData"]
    toponym_coords = toponym["Address"]["Components"][1]["name"]
    print(f'Уфа: {toponym_coords}')
else:
    print("request error")
    print(f'http code: {response.status_code} ({response.reason})')

# Нижний Новгород
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Нижний Новгород&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
        "GeocoderMetaData"]
    toponym_coords = toponym["Address"]["Components"][1]["name"]
    print(f'Нижний Новгород: {toponym_coords}')
else:
    print("request error")
    print(f'http code: {response.status_code} ({response.reason})')

# Калининград
geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Калининград&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
        "GeocoderMetaData"]
    toponym_coords = toponym["Address"]["Components"][1]["name"]
    print(f'Калининград: {toponym_coords}')
else:
    print("request error")
    print(f'http code: {response.status_code} ({response.reason})')