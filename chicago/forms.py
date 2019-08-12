from wtforms import Form, StringField, SubmitField, validators
from flask_wtf import FlaskForm
from wtforms.validators import input_required

class SearchOld(FlaskForm):
    old_number = StringField("Old Number")
    street_name = StringField("Street Name")
    direction = StringField("Direction")
    submit = SubmitField()

class SearchNew(FlaskForm):
    new_number = StringField("New Number")
    street_name = StringField("Street Name")
    direction = StringField("Direction")
    submit = SubmitField()
    