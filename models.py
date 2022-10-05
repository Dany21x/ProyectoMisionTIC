from database import db

'''
Para actualizar:
flask db stamp head -obtener ultima version
flask db migrate
flask db upgrade
'''


class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    id_country = db.Column(db.Integer)
    id_department = db.Column(db.Integer)
    id_city = db.Column(db.Integer)

class LostPet(db.Model):
    id_lost_pet = db.Column(db.Integer, primary_key=True)
    pet_type = db.Column(db.String(100))
    pet_name = db.Column(db.String(100))
    pet_breed = db.Column(db.String(100))
    int_pet_age = db.Column(db.Integer)
    um_pet_age = db.Column(db.String(100))
    pet_color = db.Column(db.String(100))
    location = db.Column(db.String(100))
    id_country = db.Column(db.Integer)
    id_department = db.Column(db.Integer)
    id_city = db.Column(db.Integer)
    last_seen = db.Column(db.DateTime)
    contact_numer = db.Column(db.Integer)
    description = db.Column(db.String(500))
    url_pet_image = db.Column(db.String(500))

class Country(db.Model):
    id_country = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100))

class Department(db.Model):
    id_department = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(100))
    id_country = db.Column(db.Integer, db.ForeignKey('country.id_country'))

class City(db.Model):
    id_city = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100))
    state = db.Column(db.Integer)
    id_department = db.Column(db.Integer, db.ForeignKey('department.id_department'))