from wtforms import Form, StringField, SubmitField, SelectField, RadioField, validators
from flask_wtf import FlaskForm
from wtforms.validators import input_required

class SearchOld(FlaskForm):
    old_number = StringField("Old Number")
    street_name = StringField("Street Name")
    direction = SelectField("Direction", choices=[('n', 'N'), ('s', 'S'), ('e', 'E'), ('w', 'W')])
    old_street_type = SelectField("Street Type", choices=[('Street', 'Street'), ('Alley', 'Alley'), ('Lane', 'Lane'), ('Avenue', 'Avenue'), ('Place', 'Place'), ('Boulevard', 'Boulevard'), ('Way', 'Way'), ('Plaza', 'Plaza'), ('Drive', 'Drive'), ('Road', 'Road'), ('na', 'na')])
    submit = SubmitField()

class SearchNew(FlaskForm):
    new_number = StringField("New Number")
    street_name = StringField("Street Name")
    direction = SelectField("Direction", choices=[('n', 'N'), ('s', 'S'), ('e', 'E'), ('w', 'W')])
    new_street_type = SelectField("Street Type", choices=[('Street', 'Street'), ('Avenue', 'Avenue'), ('Alley', 'Alley'), ('Lane', 'Lane'), ('Place', 'Place'), ('Boulevard', 'Boulevard'), ('Way', 'Way'), ('Plaza', 'Plaza'), ('Drive', 'Drive'), ('Road', 'Road'), ('na', 'na')])
    submit = SubmitField()