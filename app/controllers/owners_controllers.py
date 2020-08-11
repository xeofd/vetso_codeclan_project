# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request,  session
from models.owner import Owner
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
import repositories.note_repository as NR
import repositories.pet_type_repository as PTR

# Create blueprint
owners_blueprint = Blueprint('owners', __name__)

# Set session error logging
def return_error(error):
    # set session
    session['error_message'] = 'EC: ' + error + ' - Could not add object to database. Please try again'
    # Redirect the user
    return redirect('/owners')

# Routes

# INDEX
@owners_blueprint.route('/owners')
def index():
    # Check for session
    session_exists = session.get('error_message')

    if session_exists != None:
        error_message = session_exists
        session.pop('error_message')
    else:
        error_message = None

    owners = OR.select_all()
    return render_template('owners/index.html', title='Owners', owners=owners, error_message=error_message)

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

    if len(first_name) > 48:
        return_error('ao-1') # Return error code 1: Firstname too long
    elif len(last_name) > 48:
        return_error('ao-2') # Return error code 2: Lastname too long
    elif len(email) > 100:
        return_error('ao-3') # Return error code 3: Email address too long
    elif len(contact_no) > 11:
        return_error('ao-4') # Return error code 4: Contact number too long
    elif len(address) > 100:
        return_error('ao-5') # Return error code 5: Address too long
    elif len(post_code) > 8:
        return_error('ao-6') # Return error code 6: Post code too long
    elif len(city) > 100:
        return_error('ao-7') # Return error code 7: City too long

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
    return redirect('/owners/'+id)

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

    if len(first_name) > 48:
        return_error('eo-1') # Return error code 1: Firstname too long
    elif len(last_name) > 48:
        return_error('eo-2') # Return error code 2: Lastname too long
    elif len(email) > 100:
        return_error('eo-3') # Return error code 3: Email address too long
    elif len(contact_no) > 11:
        return_error('eo-4') # Return error code 4: Contact number too long
    elif len(address) > 100:
        return_error('eo-5') # Return error code 5: Address too long
    elif len(post_code) > 8:
        return_error('eo-6') # Return error code 6: Post code too long
    elif len(city) > 100:
        return_error('eo-7') # Return error code 7: City too long

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

    return redirect('/owners/'+id)