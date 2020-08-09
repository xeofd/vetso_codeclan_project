# Import required modules
from flask import Flask, Blueprint, render_template, redirect
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
    pets = PR.select_all()
    return render_template('pets/index.html', title='Pets', pets=pets)

# ADD
@pets_blueprint.route('/pets/add')
def new():
    owners = OR.select_all()
    vets = VR.select_all()
    pet_types = PTR.select_all()
    return render_template('pets/add.html', title='Add Pet', owners=owners, vets=vets, pet_types=pet_types)