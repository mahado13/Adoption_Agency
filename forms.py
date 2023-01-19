from email import message
from random import choices
from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, URL

"""
By:Mahad Osman
Date: Jan 19
Assignment: Adoption Agency 
"""

class AddPetForm(FlaskForm):
    """Form for adding a new pet!"""
    """ Validation:
        - A pet can only be one of three species 
        - Photo must be a url
        - age a pet cannot be younger than 0 or older than 30
    """
    name =StringField("Pet name:")
    species =SelectField("Species:", choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')])
    photo_url = StringField("Pet Photo:", validators=[URL(message="Please enter a proper url.")])
    age =IntegerField("Pet age:", validators=[NumberRange(min=0, max=30, message="Age must be between 0-30")]) 
    notes =StringField("Enter relevant notes:")
    available = BooleanField("Pet available?")