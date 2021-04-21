import flask

blueprint = flask.Blueprint(
    "jobs",
    __name__
)

@blueprint.route('/api/jobs')
def get():
    return "get"