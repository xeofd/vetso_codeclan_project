# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request
from models.classes import Pet
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
import repositories.note_repository as NR
import repositories.pet_type_repository as PTR

# Create blueprint
pets_blueprint = Blueprint('pets', __name__)

# Routes

# INDEX
@pets_blueprint.route('/pets')
def index():
    # Get required data from db
    pets = PR.select_all()

    # Render page
    return render_template('pets/index.html', title='Pets', pets=pets)

# ADD
@pets_blueprint.route('/pets/add')
def new():
    # Pull in the required data from other repos
    owners = OR.select_all()
    vets = VR.select_all()
    pet_types = PTR.select_all()

    # Render the page
    return render_template('pets/add.html', title='Add Pet', owners=owners, vets=vets, pet_types=pet_types)

# SAVE
@pets_blueprint.route('/pets', methods=['POST'])
def save():
    # Get the data from the form
    name = request.form['pet_name']
    dob = request.form['pet_age']
    type_id = request.form['pet_type']
    owner_id = request.form['pet_owner']
    vet_id = request.form['pet_vet']

    # Find the correct data for the Pet object
    pet_type = PTR.select(type_id)
    owner = OR.select(owner_id)
    vet = VR.select(vet_id)

    # Create new Pet object to be saved to db
    pet = Pet(name, dob, owner, pet_type, vet)
    PR.save(pet)

    return redirect('/pets')