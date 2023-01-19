from models import db, connect_db, Pet
from app import app

"""
Author: Mahad Osman
Date: Jan 11th 2023
Assignment Blogly part 2
"""

#Create all tables 
db.drop_all()
db.create_all()

"""Our Pet inserts """
#Pet(name="", species = "", photo_url=, age="", notes="", available=)

p1= Pet(name="Kitty Pride", species = "cat", photo_url="https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80", age=3, available=True)
p2= Pet(name="Super Dog", species = "dog", photo_url="https://images.unsplash.com/photo-1493916665398-143bdeabe500?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fGFuaW1hbHN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60", age=4,  available=True)
p3= Pet(name="Yogi Bear", species = "bear", photo_url="https://images.unsplash.com/photo-1589656966895-2f33e7653819?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YW5pbWFsc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", age=5,  available=True)


db.session.add_all([p1,p2,p3])
db.session.commit()
