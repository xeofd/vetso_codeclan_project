# Import required modules
from flask import Flask, Blueprint, render_template, redirect, request
import repositories.treatment_repository as TR
from models.treatment import Treatment

# Create blueprint
treatment_blueprint = Blueprint('treatments', __name__)

# Routes

# ADD
@treatment_blueprint.route('/treatments/add')
def add():
    return render_template('treatments/add.html', title='Add a treatment')

# SAVE
@treatment_blueprint.route('/treatments/add', methods=['POST'])
def save():
    # Grab the data from the form
    name = request.form['treatment_name']
    cost = float(request.form['treatment_cost'])
    length = int(request.form['treatment_length'])
    medicine = request.form['treatment_medicine']
    treatment_type = request.form['treatment_type']

    # Create treatment object to save
    treatment = Treatment(name, cost, length, medicine, treatment_type)
    TR.save(treatment)

    return redirect('/')