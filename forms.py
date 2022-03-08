from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, NumberRange

pet_species = ['Dog', 'Cat', 'Rabbit', 'Iguana', 'Tarantula', 'Hamster', 'Chameleon', 'Ferret', 'Bird','Guinea Pig', 'Fish', 'Turtle', 'Amphibian', 'Repitle', 'Parrot', 'Chinchilla', 'Gerbil', 'Parakeet', 'Frog', 'Tortoise', 'Snake', 'Gecko', 'Anole']

class PetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField('Pet Name', validators=[InputRequired(message="Please add a name")])
    species = SelectField('Species', choices=[(sp, sp) for sp in pet_species])
    photo_url = StringField('Pet Image', validators=[InputRequired(message="Please add an image of the pet")])
    age = FloatField('Age', validators=[NumberRange(min=0, max=30, message="Please enter age between 0 to 30")])
    notes = StringField('Notes')
    avaliable = BooleanField('Avalibility')


