import math
import requests

def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)
    return distance

if __name__ == "__main__":
    print('Введите адрес дома')
    home = input()
    print('Введите адрес школы')
    school = input()

    response = requests.get("https://geocode-maps.yandex.ru/1.x/?apikey="
                            "40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + home + "&format=json")
    json_response = response.json()
    a = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

    response = requests.get("https://geocode-maps.yandex.ru/1.x/?apikey="
                            "40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + school + "&format=json")
    json_response = response.json()
    b = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

    d = lonlat_distance((float(a[0]), float(a[1])), (float(b[0]), float(b[1])))
    print(d, "метров")