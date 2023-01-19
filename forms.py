from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional

"""
By:Mahad Osman
Date: Jan 19
Assignment: Adoption Agency 
"""

class AddPetForm(FlaskForm):
    """Form for adding a new pet!"""
    name =StringField("Pet name:")
    species =StringField("Species:")
    photo_url = StringField("Pet Photo:")
    age =IntegerField("Pet age:") 
    notes =StringField("Enter relevant notes:")
    available = BooleanField("Pet available?")