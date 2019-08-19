from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from flask_login import LoginManager
import pandas as pd


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SECRET_KEY'] = "go do your research"