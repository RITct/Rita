from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    input_data = StringField('openid', validators=[DataRequired()])