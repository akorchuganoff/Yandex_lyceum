from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    team_leader = IntegerField('Team Leader id', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    category = SelectField('Category id', validators=[DataRequired()], choices=[1, 2, 3])
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Submit')
