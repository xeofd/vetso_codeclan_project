# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request
from models.owner import Owner
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
import repositories.note_repository as NR
import repositories.pet_type_repository as PTR

# Create blueprint
owners_blueprint = Blueprint('owners', __name__)

# Routes

# INDEX
@owners_blueprint.route('/owners')
def index():
    owners = OR.select_all()
    return render_template('owners/index.html', title='Owners', owners=owners)

# ADD
@owners_blueprint.route('/owners/add')
def add():
    return render_template('/owners/add.html', title='Add an Owner')

# SAVE
@owners_blueprint.route('/owners', methods=['POST'])
def save():
    # Get data from request
    first_name = request.form['owner_first_name']
    last_name = request.form['owner_last_name']
    email = request.form['owner_email']
    contact_no = request.form['owner_contact_number']
    address = request.form['owner_address']
    post_code = request.form['owner_post_code']
    city = request.form['owner_city']

    # Create new owner object to be saved
    owner = Owner(first_name, last_name, email, contact_no, address, post_code, city, True)
    OR.save(owner)

    return redirect('/owners')

# VIEW
@owners_blueprint.route('/owners/<id>')
def view(id):
    # Get data to be displayed
    owner = OR.select(id)
    pets = PR.select_by_owner(id)
    pet_count = len(pets)

    return render_template('owners/specific.html', title=owner.first_name + " " + owner.last_name, owner=owner, pets=pets, pet_count=pet_count)

# DELETE
@owners_blueprint.route('/owners/<id>/delete', methods=['POST'])
def delete(id):
    # Run delete function and redirect
    OR.delete(id)

    # Redirect user
    return redirect('/owners')

# EDIT
@owners_blueprint.route('/owners/<id>/edit')
def edit(id):
    # Get data needed
    owner = OR.select(id)

    # Render template
    return render_template('owners/edit.html', title='Edit'+owner.first_name+" "+owner.last_name, owner=owner)

# UPDATE
@owners_blueprint.route('/owners/<id>', methods=['POST'])
def update(id):
    # Get data from request
    first_name = request.form['owner_first_name']
    last_name = request.form['owner_last_name']
    email = request.form['owner_email']
    contact_no = request.form['owner_contact_number']
    address = request.form['owner_address']
    post_code = request.form['owner_post_code']
    city = request.form['owner_city']

    # check checkbox exists
    checkbox = request.form.get("owner_registered")

    if checkbox is not None:
        print("Found")
        registered = True
        print(registered)
    else:
        print("Not found")
        registered = False
        print(registered)

    # Create the updated object
    owner = Owner(first_name, last_name, email, contact_no, address, post_code, city, registered, id)
    OR.update(owner)

    return redirect('/owners')