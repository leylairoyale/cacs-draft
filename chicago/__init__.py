from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from flask_login import LoginManager
import pandas as pd


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# if you switch to elephantsql, then you will change the sqlite link below to the one that elephant
# will give you so it will hook up to the db gthat way via sqlalchemy. joel recommends using this
# over aws.

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SECRET_KEY'] = "go do your research"