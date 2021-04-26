from flask import jsonify
from . import db_session
from .colonists import User
from .parser import parser
from flask_restful import abort, Resource



def abort_if_email_exist(user_email):
    session = db_session.create_session()
    user = session.query(User).filter(User.email == user_email).first()
    if user:
        abort(409, message=f"Email {user_email} exist")



def abort_if_id_exist(user_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        abort(409, message=f"User {user_id} exist")




def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")





class UserResource(Resource):
    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'surname', 'name', 'age', 'position',
                  'speciality', 'address', 'email', 'city_from'))})







class UsersListResource(Resource):
    def post(self):
        args = parser.parse_args()
        abort_if_id_exist(args['id'])
        abort_if_email_exist(args['email'])
        session = db_session.create_session()
        user = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            city_from=args['city_from']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'position',
                  'speciality', 'address', 'email', 'city_from')) for item in users]})
