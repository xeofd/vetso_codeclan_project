# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request
from models.classes import Vet
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
import repositories.note_repository as NR
import repositories.pet_type_repository as PTR

# Create the blueprint
vets_blueprint = Blueprint('vets', __name__)

# Routes

# INDEX
@vets_blueprint.route('/vets')
def index():
    # Grab the correct data
    vets = VR.select_all()

    # Render the page
    return render_template('vets/index.html', title='Vets', vets=vets)

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
    return redirect('/vets')