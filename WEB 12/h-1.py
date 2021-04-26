from flask import jsonify
from . import db_session
from .jobs import Jobs
from .colonists import User
from .category import Category
from .jobs_parser import parser
from flask_restful import abort, Resource





def abort_if_category_not_exist(category_id):
    session = db_session.create_session()
    category = session.query(Category).filter(Category.id == category_id).first()
    if not category:
        abort(409, message=f"Category {category_id} doesn't exist")


def abort_if_id_exist(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).filter(Jobs.id == job_id).first()
    if job:
        abort(409, message=f"Job {job_id} exist")



def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")



def abort_if_team_leader_not_exist(team_leader_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == team_leader_id).first()
    if not user:
        abort(409, message=f"User {team_leader_id} doesn't exist")





class JobsResource(Resource):


    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
                  'is_finished'))})




class JobsListResource(Resource):


    def post(self):
        args = parser.parse_args()
        abort_if_id_exist(args['id'])
        abort_if_team_leader_not_exist(args['team_leader'])
        abort_if_category_not_exist(args['categories'])
        session = db_session.create_session()
        job = Jobs(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        category = session.query(Category).filter(Category.id == args['categories']).first()
        job.categories.append(category)
        session.commit()
        return jsonify({'success': 'OK'})


    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
                  'is_finished')) for item in jobs]})