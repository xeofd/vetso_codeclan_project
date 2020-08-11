# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request, session
from models.vet import Vet
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
import repositories.note_repository as NR
import repositories.pet_type_repository as PTR

# Create the blueprint
vets_blueprint = Blueprint('vets', __name__)

# Set session error logging
def return_error(error):
    # set session
    session['error_message'] = 'EC: ' + error + ' - Could not add object to database. Please try again'
    # Redirect the user
    return redirect('/vets')

# Routes

# INDEX
@vets_blueprint.route('/vets')
def index():
    # Check for session
    session_exists = session.get('error_message')

    if session_exists != None:
        error_message = session_exists
        session.pop('error_message')
    else:
        error_message = None

    # Grab the correct data
    vets = VR.select_all()

    # Render the page
    return render_template('vets/index.html', title='Vets', vets=vets, error_message=error_message)

# ADD
@vets_blueprint.route('/vets/add')
def add():
    # render the page
    return render_template('vets/add.html', title='Add a vet')

# SAVE
@vets_blueprint.route('/vets', methods=['POST'])
def save():
    # Grab data from request
    first_name = request.form['vet_first_name']
    last_name = request.form['vet_last_name']

    if len(first_name) > 48:
        return_error('av-1') # Return error code 1: First name too long
    elif len(last_name) > 48:
        return_error('av-2') # Return error code 2: Last name too long

    # Create new object to be saved
    vet = Vet(first_name, last_name)
    VR.save(vet)

    # Redirect the user
    return redirect('/vets')

# VIEW
@vets_blueprint.route('/vets/<id>')
def view(id):
    # Grab needed data
    vet = VR.select(id)
    pets = PR.select_by_vet(id)
    pet_count = len(pets)

    # Render page
    return render_template('vets/specific.html', title=vet.first_name+" "+vet.last_name, vet=vet, pets=pets, pet_count=pet_count)

# DELETE
@vets_blueprint.route('/vets/<id>/delete', methods=['POST'])
def delete(id):
    # Run the delete function
    VR.delete(id)
    return redirect('/vets/'+id)

# EDIT
@vets_blueprint.route('/vets/<id>/edit')
def edit(id):
    # Grab needed data
    vet = VR.select(id)
    
    # Render page
    return render_template('vets/edit.html', title='Edit '+vet.first_name+' '+vet.last_name, vet=vet)

# UPDATE
@vets_blueprint.route('/vets/<id>', methods=['POST'])
def update(id):
    # Grab data from request
    first_name = request.form['vet_first_name']
    last_name = request.form['vet_last_name']

    if len(first_name) > 48:
        return_error('ev-1') # Return error code 1: First name too long
    elif len(last_name) > 48:
        return_error('ev-2') # Return error code 2: Last name too long

    # Create new object to be saved
    vet = Vet(first_name, last_name, id)
    VR.update(vet)

    # Redirect the user
    return redirect('/vets/'+id)