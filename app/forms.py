from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class GrantForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
