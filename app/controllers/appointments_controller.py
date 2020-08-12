# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request, session
from models.appointment import Appointment
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.appointment_repository as AR

# Create blueprint
appointments_blueprint = Blueprint('appointments', __name__)

# Routes

# ADD
@appointments_blueprint.route('/appointments/add')
def new():
    # Pull in the required data from other repos
    vets = VR.select_all()
    pets = PR.select_all()

    # Render the page
    return render_template('appointments/add.html', title='Create appointment', vets=vets, pets=pets)

# SAVE
@appointments_blueprint.route('/appointments/add', methods=['POST'])
def save():
    # Grab request data
    date = request.form['appointment_date']
    note = request.form['appointment_note']
    vet_id = request.form['appointment_vet']
    pet_id = request.form['appointment_pet']

    # Grab needed objects
    vet = VR.select(vet_id)
    pet = PR.select(pet_id)

    # Create object for saving
    appointment = Appointment(date, note, pet, vet, pet)
    AR.save(appointment)

    # Redirect
    return redirect('/pets/'+pet_id)

# SAVE FROM PET
@appointments_blueprint.route('/appointments/add/<id>', methods=['POST'])
def save_from_pet(id):
    # Grab request data
    date = request.form['appointment_date']
    note = request.form['appointment_note']
    vet_id = request.form['appointment_vet']

    # Grab needed objects
    vet = VR.select(vet_id)
    pet = PR.select(id)

    # Create object for saving
    appointment = Appointment(date, note, pet, vet, pet)
    AR.save(appointment)

    # Redirect
    return redirect('/pets/'+id)