from flask import make_response, jsonify, Blueprint, abort, request, render_template, redirect
from data import db_session
from data.jobs import Jobs
from data.category import Category
from forms.jobs import JobsForm
import datetime

blueprint = Blueprint(
    "jobs",
    __name__
)

@blueprint.route('/api/jobs', methods=['POST', 'GET'])
def get_all():
    if request.method == 'GET':
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
        job_list = []
        for job in jobs:
            job_list.append(job.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')))
        if job_list:
            return make_response(jsonify(job_list), 200)
        else:
            abort(404)
    elif request.method == 'POST':
        if not request.json:
            return jsonify({'error': 'Empty request'})

        elif not all(key in request.json for key in
                     ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
            return jsonify({'error': 'Bad request'})

        for key in request.json:
            print(key)

        db_sess = db_session.create_session()

        job = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()
        if job:
            return jsonify({'error': 'Id already exists'})

        job = Jobs(

            collaborators=request.json['collaborators'],
            is_finished=request.json['is_finished'],
            job=request.json['job'],
            id=request.json['id'],
            work_size=request.json['work_size'],
            team_leader=request.json['team_leader']

        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET', "DELETE", "PUT"])
def get_one(job_id):
    if request.method == 'GET':
        db_sess = db_session.create_session()
        if type(job_id) != int:
            return make_response(jsonify({'message': 'wrong type of arguement'}))
        jobs = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        if jobs:
            return make_response(jsonify(jobs.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))), 200)
        else:
            return make_response(jsonify({'message': 'wrong id'}))
    elif request.method == 'DELETE':
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        if job:
            db_sess.delete(job)
            db_sess.commit()
            return make_response(jsonify({'success': 'OK'}))
        else:
            return make_response(jsonify({'error': 'There is no jobs with current id'}))

    elif request.method == 'PUT':
        db_sess = db_session.create_session()

        job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        if not job:
            return jsonify({'error': 'Can not find job'})


        for key in request.json:
            if key == 'collaborators':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                job.collaborators = request.json['collaborators']
            elif key == 'is_finished':
                if type(request.json[key]) != bool:
                    return make_response(jsonify({'error': 'different type'}))
                job.is_finished = request.json['is_finished']
            elif key == 'job':
                if type(request.json[key]) != str:
                    return make_response(jsonify({'error': 'different type'}))
                job.job = request.json['job']
            elif key == 'work_size':
                if type(request.json[key]) != int:
                    return make_response(jsonify({'error': 'different type'}))
                job.work_size = request.json['work_size']
            elif key == 'team_leader':
                if type(request.json[key]) != int:
                    return make_response(jsonify({'error': 'different type'}))
                job.team_leader = request.json['team_leader']
            elif key == 'start_date':
                if type(request.json[key]) != datetime.datetime:
                    return make_response(jsonify({'error': 'different type'}))
                job.start_date = request.json['start_date']
            elif key == 'end_date':
                if type(request.json[key]) != datetime.datetime:
                    return make_response(jsonify({'error': 'different type'}))
                job.end_date = request.json['end_date']
            else:
                return make_response(jsonify({'error': 'strange field'}))
        db_sess.commit()
        return jsonify({'success': 'OK'})