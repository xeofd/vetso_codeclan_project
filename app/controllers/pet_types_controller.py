# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request
from models.pet_type import PetType
import repositories.pet_type_repository as PTR

# Create blueprint
pet_type_blueprint = Blueprint('pet_types', __name__)

# Routes

# ADD
@pet_type_blueprint.route('/pet-types/add')
def add():
    return render_template('pet_types/add.html', title='Add a pet type')

# SAVE
@pet_type_blueprint.route('/pet-types/add', methods=['POST'])
def save():
    # Grab the data from the form
    animal_type = request.form['pet_type']
    animal_breed = request.form['pet_breed']
    # Create pet_type object to save
    pet_type = PetType(animal_type, animal_breed)
    PTR.save(pet_type)

    return redirect('/')