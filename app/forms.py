from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class GrantForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
