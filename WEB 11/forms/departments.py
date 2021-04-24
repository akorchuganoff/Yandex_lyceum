from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Department Title', validators=[DataRequired()])
    chief = IntegerField('Chief id', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = StringField('Department Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
