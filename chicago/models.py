from chicago import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Address(db.Model):
    __tablename__ = 'Address'
    id = db.Column(db.Integer, primary_key=True)
    new_num = db.Column(db.String)
    new_dir = db.Column(db.String(1))
    new_street = db.Column(db.String)
    old_num = db.Column(db.String)
    old_dir = db.Column(db.String(1))
    old_street = db.Column(db.String)
    duplicate = db.Column(db.String)


    def __init__(self, new_num, new_dir, new_street, old_num, old_street, old_dir, duplicate):
        self.new_num = new_num
        self.new_dir = new_dir
        self.new_street = new_street
        self.old_num = old_num
        self.old_dir = old_dir
        self.old_street = old_street
        self.duplicate = duplicate

    def __repr__(self):
        self.new_num = new_num
        self.new_dir = new_dir
        self.new_street = new_street
        self.old_num = old_num
        self.old_dir = old_dir
        self.old_street = old_street
        self.duplicate = duplicate

    # # trying to add a csv to the database
    # def add_carmen_csv():
    #     df = pd.read_csv('chicago\cacs_carmen_ave.csv')
    #     df.to_sql(con=engine, index_label='id', name=Address.__tablename__, if_exists='replace')
