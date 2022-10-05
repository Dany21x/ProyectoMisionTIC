from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, \
                    IntegerField, DateTimeField, SelectMultipleField, \
                    SelectField, PasswordField
from wtforms.fields import DateTimeLocalField, DateTimeField
from wtforms.validators import DataRequired, InputRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserForm(FlaskForm):
    first_name = StringField('Nombre', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Apellido', validators=[DataRequired()])
    user_name = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    id_country = SelectField('País', choices=[], validators=[DataRequired()])
    id_department = SelectField('Departamento', choices=[], validators=[DataRequired()])
    id_city = SelectField('Ciudad', choices=[], validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class LostPetForm(FlaskForm):
    pet_type = SelectField('Tipo de mascota', choices=[('',''),(1,'Perro'),(2,'Gato')], validators=[DataRequired()])
    pet_name = StringField('Nombre', validators=[DataRequired()])
    pet_breed = SelectField('Raza', choices=[('',''),(1,'Labrador'),(2,'Criollo')], validators=[DataRequired()])
    int_pet_age = IntegerField('Edad')
    um_pet_age = SelectField('Meses-Años', choices=[('',''),(1,'Meses'),(2,'Años')])
    pet_color = StringField('Color', validators=[DataRequired()])
    id_country = SelectField('Country', choices=[], validators=[DataRequired()])
    id_department = SelectField('Department', choices=[], validators=[DataRequired()])
    id_city = SelectField('City', choices=[], validators=[DataRequired()])
    location = StringField('Visto por última vez en:', validators=[DataRequired()])
    last_seen = DateTimeLocalField('Visto por última vez el día', format="%Y-%m-%dT%H:%M", validators=[InputRequired()])
    contact_numer = IntegerField('Número de contacto')
    description = StringField('Descripción', validators=[DataRequired()], widget=TextArea())
    url_pet_image = FileField('Foto', validators=[FileAllowed(['jpg','jpeg','png']), FileRequired()])
    submit = SubmitField('Publicar')