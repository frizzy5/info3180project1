from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "$$tarz"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pro1:password@localhost/pro1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models