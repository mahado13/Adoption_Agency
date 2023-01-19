from enum import auto, unique

from sqlalchemy import null
from flask_sqlalchemy import SQLAlchemy 
"""
By:Mahad Osman
Date: Jan 19
Assignment: Adoption Agency 
"""

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Table"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable = True, unique=True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String, nullable = True)
    available = db.Column(db.Boolean)

    def __repr__(self) -> str:
        p = self
        return f"<Pet Name = {p.name} species ={p.species} age={p.age}"