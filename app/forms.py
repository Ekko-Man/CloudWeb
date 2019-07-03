from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    username = StringField('User Name', validators=[DataRequired()])
    submit = SubmitField('Register')