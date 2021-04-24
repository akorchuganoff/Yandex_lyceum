from flask import make_response, jsonify, Blueprint, abort, request, render_template, redirect
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


@blueprint.route('/api/user', methods=['POST', 'GET'])
def get_all():
    if request.method == 'GET':
        db_sess = db_session.create_session()
        users = db_sess.query().all()
        user_list = []
        for user in users:
            user_list.append(user.to_dict(only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password', 'modified_date')))
        if user_list:
            return make_response(jsonify(user_list), 200)
        else:
            abort(404)
    elif request.method == 'POST':
        if not request.json:
            return jsonify({'error': 'Empty request'})

        elif not all(key in request.json for key in
                     ['id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'password']):
            return jsonify({'error': 'Bad request'})

        for key in request.json:
            print(key)

        db_sess = db_session.create_session()

        user = db_sess.query(User).filter(User.id == request.json['id']).first()
        if user:
            return jsonify({'error': 'Id already exists'})

        user = User()
        user.id=request.json['id'],
        user.name='name',
        user.surname=request.json['surname'],
        user.age=request.json['age'],
        user.position=request.json['position'],
        user.speciality=request.json['speciality'],
        user.address=request.json['address'],
        user.email=request.json['email']

        user.set_password(request.json['password'])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['GET', "DELETE", "PUT"])
def get_one(user_id):
    if request.method == 'GET':
        db_sess = db_session.create_session()
        if type(user_id) != int:
            return make_response(jsonify({'message': 'wrong type of arguement'}))
        user = db_sess.query(User).filter(User.id == user_id).first()
        if user:
            return make_response(jsonify(user.to_dict(only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password'))), 200)
        else:
            return make_response(jsonify({'message': 'wrong id'}))
    elif request.method == 'DELETE':
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == user_id).first()
        if user:
            db_sess.delete(user)
            db_sess.commit()
            return make_response(jsonify({'success': 'OK'}))
        else:
            return make_response(jsonify({'error': 'There is no user with current id'}))

    elif request.method == 'PUT':
        db_sess = db_session.create_session()

        user = db_sess.query(User).filter(User.id == user_id).first()
        if not user:
            return jsonify({'error': 'Can not find user'})


        for key in request.json:
            if key == 'address':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                user.address = request.json['address']
            elif key == 'speciality':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                user.speciality = request.json['speciality']
            elif key == 'position':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                user.position = request.json['position']
            elif key == 'age':
                if type(request.json[key]) != int:
                    return make_response(jsonify({'error': 'different type'}))
                user.age = request.json['age']
            elif key == 'name':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                user.name = request.json['name']
            elif key == 'surname':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                user.surname = request.json['surname']
            elif key == 'email':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                user.email = request.json['email']
            else:
                return make_response(jsonify({'error': 'strange field'}))
        user.modified_date = datetime.datetime.now()
        db_sess.commit()
        return jsonify({'success': 'OK'})


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