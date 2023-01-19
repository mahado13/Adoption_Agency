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