from chicago import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Street(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    new_street = db.Column(db.String)
    old_street = db.Column(db.String)
    searches = db.relationship('Search', backref='Street', lazy=True)

    def __init__(self, old, new):
        self.old = old
        self.new = new
        

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old = db.Column(db.Integer)
    new = db.Column(db.Integer)
    direction = db.Column(db.String(1))
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'))


    def __init__(self, old, new, direction):
        self.old = old
        self.new = new
        self.direction = direction