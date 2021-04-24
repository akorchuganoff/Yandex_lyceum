from flask import make_response, jsonify, Blueprint, abort, request, render_template, redirect, url_for
from data import db_session
from .data.colonists import User
import requests
import datetime

blueprint = Blueprint(
    "users",
    __name__
)

map_api_server = "http://static-maps.yandex.ru/1.x/"
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"




@blueprint.route("/users_show/<int:user_id>")
def users_show(user_id):
    json_response = requests.get(f'http://localhost:5000/api/users/{user_id}').json()
    if 'error' in json_response:
        return redirect('/')
    city_name = json_response['user']['city_from']
    name = f"{json_response['user']['surname']} {json_response['user']['name']}"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": city_name,
        "format": "json"}

    try:
        response = requests.get(geocoder_api_server, params=geocoder_params)
        toponym_coordinates = response.json()["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]["Point"]["pos"]
    except Exception as e:
        print(e)
        return redirect('/')

    map_params = {
        'spn': '0.1,0.1',
        'size': '600,400',
        'll': ','.join(toponym_coordinates.split()),
        'l': 'sat'
    }
    response = requests.get(map_api_server, map_params)
    map_file = "static/img/photo.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return render_template("hometown.html", title='Hometown', name=name, city_name=city_name,
                           src=url_for('static', filename='img/photo.png'))