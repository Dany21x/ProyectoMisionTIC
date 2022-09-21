from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, \
                    IntegerField, DateTimeField, SelectMultipleField, \
                    SelectField, PasswordField
from wtforms.fields import DateTimeLocalField, DateTimeField
from wtforms.validators import DataRequired, InputRequired

class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    country = SelectField('Country', choices=[], validators=[DataRequired()])
    department = SelectField('Department', choices=[], validators=[DataRequired()])
    city = SelectField('City', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')