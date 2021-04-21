import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

geocode_request = f'http://geocode-maps.yandex.ru/1.x?geocode=Петровки, 38&apikey={API_KEY}&format=json'
response = requests.get(geocode_request)

if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]
    toponymIndex = toponym["Address"]["postal_code"]
    print(f'Петровки, 38: {toponymIndex}')
else:
    print('response error')
    print(f'http code: {response.status_code} ({response.reason})')