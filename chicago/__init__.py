from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from flask_login import LoginManager
import pandas as pd

# below two are added to get elephantsql up and running
import urllib.parse as up
import psycopg2


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# below is also added per documentation to get elephantsql up and running.
up.uses_netloc.append("postgres")
url = 'postgres://vuprceph:cMjhLw94OuYo_9zGNmovrPWraHt-tri1@salt.db.elephantsql.com:5432/vuprceph'
conn = psycopg2.connect(url)

# if you switch to elephantsql, then you will change the sqlite link below to the one that elephant
# will give you so it will hook up to the db gthat way via sqlalchemy. joel recommends using this
# over aws. you'll als have to delete the following from the below line:
# + os.path.join(basedir, 'data.db')

app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://vuprceph:cMjhLw94OuYo_9zGNmovrPWraHt-tri1@salt.db.elephantsql.com:5432/vuprceph' 
app.config['SECRET_KEY'] = "go do your research"