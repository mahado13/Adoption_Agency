"""
By:Mahad Osman
Date: Jan 19
Assignment: Adoption Agency 
"""

"""Python Requirments for this project"""

"""
1. App.py 
    Three flask routes:
    - A route for showing our list of pets
    - A route for showing an add pet form, and handling the form submission
    - A route for showing an edit pet form, and handling the form submission

    Inclusion of the flask_debugtoolbar

2. Models.py
    A model for our pets table:
    - id: auto-incrementing integer
    - name: text, required
    - species: text, required
    - photo_url: text, optional
    - age: integer, optional
    - notes: text, optional
    - available: true/false, required, should default to available


3. Seed.py
    A seed file to drop/create our database.
    - Also inserts test data we can work with.

4. Forms.py
    Our wtfform creation:
    - A pet form to add and edit a pet
        - Validation on on the petform
"""