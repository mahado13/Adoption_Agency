from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

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
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/pets/add', methods=["GET", "POSTS"])
def add_new_pet():
    return render_template('new_pet.html')