from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FieldList, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Required

age_choices = [
    ('1', 'Age 15-24'),
    ('2', 'Age 25-44'),
    ('3','Age 45-64'),
    ('4','Age 65+')]

class GrantForm(FlaskForm):
    pool = StringField('pool', validators=[DataRequired()])
    area = StringField('area', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    group = StringField('group', validators=[DataRequired()])
    amount = StringField('amount', validators=[DataRequired()])
    percent = StringField('percent', validators=[DataRequired()])


class ValueInkForm(FlaskForm):
    # age_group = StringField('What is your age group?', validators=[DataRequired()])
    age_group = SelectField(u'Field name', choices=age_choices, validators=[Required()])

    checkbox_1 = BooleanField('Importance of natural scenery and environment in defining New Zealand')
    checkbox_2 = BooleanField('Importance of agriculture and farming in defining New Zealand')
    checkbox_3 = BooleanField('Importance of New Zealand\'s history in defining New Zealand')
    checkbox_4 = BooleanField('Importance of New Zealand symbols and icons in defining New Zealand')
    checkbox_5 = BooleanField('Importance of sports and sporting achievements in defining New Zealand')
    checkbox_6 = BooleanField('Importance of art and artistic achievements in defining New Zealand')
    checkbox_7 = BooleanField('Importance of multiculturalism and ethnic diversity in defining New Zealand')
    checkbox_8 = BooleanField('Importance of Maori culture and cultural practices in defining New Zealand')
    checkbox_9 = BooleanField('Importance of the people in New Zealand in defining New Zealand')
    checkbox_10 = BooleanField('Importance of freedom, rights and peace in defining New Zealand')
