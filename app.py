from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import configure_uploads, IMAGES, UploadSet


from database import db
from forms import UserForm, LostPetForm
from models import User, LostPet, Country, Department, City

app = Flask(__name__)

#Database configuration
USER_DB = 'root'
PASS_DB = ''
URL_DB = 'localhost'
NAME_DB = 'pets_project_db'
PORT_DB = 3307
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}?charset=utf8mb4'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_IMAGES_DEST'] = 'static/upload_images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

db.init_app(app)

#COnfigure flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY'] = 'DN29m8*3D!h^'


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/register_user', methods=['GET','POST'])
@app.route('/register_user.html', methods=['GET','POST'])
def register_user():
    user = User()
    userForm = UserForm(obj=user) #Especifica la clase de modelo que vamos a asociar al formulario
    userForm.id_country.choices = [(country.id_country, country.country_name) for country in Country.query.all()]
    userForm.id_department.choices = [(department.id_department, department.department_name) for department in
                                      Department.query.all()]
    userForm.id_city.choices = [(city.id_city, city.city_name) for city in City.query.filter_by(id_department=5).all()]
    #print(City.query.filter_by(id_department=3).all())

    if request.method == 'POST':
        if userForm.validate_on_submit():
            userForm.populate_obj(user)
            app.logger.debug(f'Persona a insertar: {user}') #con populate se llena el objeto user desde el formulario
            #Insert on DB
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('register_user.html', form=userForm)


@app.route('/edit_user', methods=['GET','POST'])
@app.route('/edit_user.html', methods=['GET','POST'])
def edit_user(id_user):
    user = User.query.get_or_404(id_user)
    country = Country()
    department = Department()
    userForm = UserForm(obj=user)
    return render_template('edit_user.html', form=userForm)


@app.route('/users_list')
@app.route('/users_list.html')
def users_list():
    users = User.query.all()
    return render_template('users_list.html', users=users)


@app.route('/register_lost_pet', methods=['GET','POST'])
@app.route('/register_lost_pet.html', methods=['GET','POST'])
def register_lost_pet():
    lostPet = LostPet()
    lostPetForm = LostPetForm(obj=lostPet)
    lostPetForm.id_country.choices = [(country.id_country, country.country_name) for country in Country.query.all()]
    lostPetForm.id_department.choices = [(department.id_department, department.department_name) for department in
                                      Department.query.all()]
    lostPetForm.id_city.choices = [(city.id_city, city.city_name) for city in City.query.filter_by(id_department=5).all()]

    if request.method == 'POST':
        if lostPetForm.validate_on_submit():
            lostPetForm.populate_obj(lostPet)

            if 'url_pet_image' in request.files:
                image = request.files["url_pet_image"]
                filename = images.save(lostPetForm.url_pet_image.data)
                lostPet.url_pet_image = images.url(filename)

            app.logger.debug(f'Persona a insertar: {lostPet}') #con populate se llena el objeto user desde el formulario
            #Insert on DB
            db.session.add(lostPet)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('register_lost_pet.html', form=lostPetForm)


@app.route('/city/<id_department>')
def city(id_department):
    cities = City.query.filter_by(id_department=id_department).all()

    cityArray = []

    for city in cities:
        cityObj = {}
        cityObj['id'] = city.id_city
        cityObj['name'] = city.city_name
        cityArray.append(cityObj)

    return jsonify({'cities' : cityArray})

@app.route('/show_pets')
@app.route('/show_pets.html')
def show_pets():
    pets = LostPet.query.all()
    return render_template('show_pets.html', pets=pets)

if __name__ == '__main__':
    app.run(debug=True)