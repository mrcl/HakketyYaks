from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FieldList, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Required

age_choices = [
    ('Age 15-24', 'Age 15-24'),
    ('Age 25-44', 'Age 25-44'),
    ('Age 45-64', 'Age 45-64'),
    ('Age 65+', 'Age 65+')]


class GrantForm(FlaskForm):
    pool = StringField('pool', validators=[DataRequired()])
    area = StringField('area', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    group = StringField('group', validators=[DataRequired()])
    amount = StringField('amount', validators=[DataRequired()])
    percent = StringField('percent', validators=[DataRequired()])


class ValueInkForm(FlaskForm):
    # age_group = StringField('What is your age group?', validators=[DataRequired()])
    age_group = SelectField(u'What is your age group?', choices=age_choices, validators=[Required()])

    checkbox_1 = BooleanField(u'Importance of natural scenery and environment in defining New Zealand')
    checkbox_2 = BooleanField(u'Importance of agriculture and farming in defining New Zealand')
    checkbox_3 = BooleanField(u'Importance of New Zealand\'s history in defining New Zealand')
    checkbox_4 = BooleanField(u'Importance of New Zealand symbols and icons in defining New Zealand')
    checkbox_5 = BooleanField(u'Importance of sports and sporting achievements in defining New Zealand')
    checkbox_6 = BooleanField(u'Importance of art and artistic achievements in defining New Zealand')
    checkbox_7 = BooleanField(u'Importance of multiculturalism and ethnic diversity in defining New Zealand')
    checkbox_8 = BooleanField(u'Importance of Maori culture and cultural practices in defining New Zealand')
    checkbox_9 = BooleanField(u'Importance of the people in New Zealand in defining New Zealand')
    checkbox_10 = BooleanField(u'Importance of freedom, rights and peace in defining New Zealand')
