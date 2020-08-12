# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request, session
from models.pet import Pet
from models.note import Note
from models.treatment import PerscribedTreatment
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
import repositories.note_repository as NR
import repositories.pet_type_repository as PTR
import repositories.perscribed_treatments_repository as perscribed
import repositories.treatment_repository as TR
import repositories.appointment_repository as AR

# Create blueprint
pets_blueprint = Blueprint('pets', __name__)

# Set session error logging
def return_error(error):
    # set session
    session['error_message'] = 'EC: ' + error + ' - Could not add object to database. Please try again'
    # Redirect the user
    return redirect('/vets')

# Routes

# INDEX
@pets_blueprint.route('/pets')
def index():
    # Check for session
    session_exists = session.get('error_message')

    if session_exists != None:
        error_message = session_exists
        session.pop('error_message')
    else:
        error_message = None
    # Get required data from db
    pets = PR.select_all()

    # Get pet ages
    for pet in pets:
        pet.convert_dob_to_age()

    # Render page
    return render_template('pets/index.html', title='Pets', pets=pets, error_message=error_message)

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

    if len(name) > 64:
        return_error('ap-1') # Return error code 1: Name too long
    elif type_id == 'None':
        return_error('ap-2') # Return error code 2: No Type chosen
    elif owner_id == 'None':
        return_error('ap-3') # Return error code 3: No Owner chosen
    elif vet_id == 'None':
        return_error('ap-4') # Return error code 4: No Vet chosen

    # Find the correct data for the Pet object
    pet_type = PTR.select(type_id)
    owner = OR.select(owner_id)
    vet = VR.select(vet_id)

    if (owner.registered == False):
        return_error('ap-5') # Return error code 5: Cannot add as owner not registered

    # Create new Pet object to be saved to db
    pet = Pet(name, dob, owner, pet_type, vet)
    PR.save(pet)
    return redirect('/pets')

# VIEW
@pets_blueprint.route('/pets/<id>')
def view(id):
    # Get data for the correct pet
    pet = PR.select(id)
    notes = NR.select_by_pet(id)
    notes_length = len(notes)
    treatments = perscribed.select_by_pet(pet.id)
    treatments_length = len(treatments)
    appointments = AR.select_by_pet(id)
    appointment_length = len(appointments)

    for appointment in appointments:
        appointment.days_until()

    pet_dob_string = pet.convert_dob_to_text()

    return render_template('/pets/specific.html', title=pet.name + " - " + pet.pet_type.breed, pet_dob_string=pet_dob_string, pet=pet, notes=notes, notes_length=notes_length, treatments=treatments, treatments_length=treatments_length, appointments=appointments, appointment_length=appointment_length)

# EDIT
@pets_blueprint.route('/pets/<id>/edit')
def edit(id):
    # Pull in the required data from other repos
    pet = PR.select(id)
    owners = OR.select_all()
    vets = VR.select_all()
    pet_types = PTR.select_all()

    # Render the page
    return render_template('pets/edit.html', title='Edit Pet', pet=pet, owners=owners, vets=vets, pet_types=pet_types)

# UPDATE
@pets_blueprint.route('/pets/<id>', methods=['POST'])
def update(id):
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
    pet = Pet(name, dob, owner, pet_type, vet, id)
    PR.update(pet)

    return redirect('/pets/'+id)

# DELETE
@pets_blueprint.route('/pets/<id>/delete', methods=['POST'])
def delete(id):
    PR.delete(id)
    return redirect('/pets')

# ADD NOTE
@pets_blueprint.route('/pets/<id>/add-note')
def add_note(id):
    # Pull in the required data from other repos
    pet = PR.select(id)
    vets = VR.select_all()

    # Render the page
    return render_template('pets/add-note.html', title='Add a note to ' + pet.name, pet=pet, vets=vets)

# SAVE NOTE
@pets_blueprint.route('/pets/<id>/add-note', methods=['POST'])
def save_note(id):
    note_date = request.form['note_date']
    note_text = request.form['note_text']
    vet_id = request.form['note_vet']

    # Grab the data for the object
    pet = PR.select(id)
    vet = VR.select(vet_id)

    # Create the note object for saving
    note = Note(note_date, note_text, pet, vet)
    NR.save(note)

    # Redirect
    return redirect('/pets/'+id)

# ADD TREATMENT
@pets_blueprint.route('/pets/<id>/add-treatment')
def add_treatment(id):
    # Grab needed data
    pet = PR.select(id)
    treatments = TR.select_all()

    # Render page
    return render_template('pets/add-treatment.html', title='Add treatment to '+pet.name, treatments=treatments, pet=pet)

# SAVE TREATMENT
@pets_blueprint.route('/pets/<id>/add-treatment', methods=['POST'])
def save_treatment(id):
    # Pull in POST data
    treatment_id = request.form['treatment_id']

    # Pull in database data
    pet = PR.select(id)
    treatment = TR.select(treatment_id)

    # Save to perscribed treatments
    perscribed_treatment = PerscribedTreatment(pet, treatment)
    perscribed.save(perscribed_treatment)

    return redirect('/pets/'+id)

# ADD APPOINTMENT
@pets_blueprint.route('/pets/<id>/add-appointment')
def add_appointment(id):
    # Pull data from db
    pet = PR.select(id)
    vets = VR.select_all()

    # Render html
    return render_template('pets/add-appointment.html', title='Create appointment for '+pet.name, pet=pet, vets=vets)