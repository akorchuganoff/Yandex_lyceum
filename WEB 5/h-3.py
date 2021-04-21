import requests
import sys
# python h-3.py Барнаул Попова 106

toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym_coodrinates = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]["Point"]["pos"]
x1, y1 = toponym_coodrinates.split()

toponym_to_find = ",".join([x1, y1])

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "kind": "district",
    "format": "json"
}

response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
# print(json_response)

text = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-1]["name"]
print(text)