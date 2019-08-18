from chicago import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    new_num = db.Column(db.String)
    new_dir = db.Column(db.String(1))
    new_street = db.Column(db.String)
    old_num = db.Column(db.String)
    old_street = db.Column(db.String)
    old_dir = db.Column(db.String(1))


    def __init__(self, new_num, new_dir, new_street, old_num, old_street, old_dir):
        self.new_num = new_num
        self.new_dir = new_dir
        self.new_street = new_street
        self.old_num = old_num
        self.old_dir = old_dir
        self.old_street = old_street