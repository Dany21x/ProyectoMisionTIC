from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from database import db

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

db.init_app(app)

#COnfigure flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY'] = 'DN29m8*3D!h^'


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/register_user.html')
def register_user():
    return render_template('register_user.html')


if __name__ == '__main__':
    app.run(debug=True)