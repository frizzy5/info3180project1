from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://yecsapnzlttgcb:8860d3512549e3ebba04aa68ede74496e30041ff458ea1d46d7c4ed7f5402af0@ec2-54-221-244-196.compute-1.amazonaws.com:5432/d9d6gbbcjoc71g"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views , models

