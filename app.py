from crypt import methods
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

"""
By:Mahad Osman
Date: Jan 19
Assignment: Adoption Agency 
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "secert123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    """Our home page which will show a list of our current pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/pets/add', methods=["GET", "POST"])
def add_new_pet():
    """Our route to add a new pet, and retrieve the form to do so."""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        pet_photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=pet_photo, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet.html', form = form)


@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Displays and edit form for a pet, and handles the edit"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = pet.name
        pet.age = pet.age
        pet.species = pet.species
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/') 
    else:
        return render_template("edit_pet.html", form=form, pet=pet)