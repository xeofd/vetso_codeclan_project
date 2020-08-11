# Import required modules
from flask import Flask, Blueprint, render_template
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
from controllers.pets_controller import pets_blueprint
from controllers.owners_controllers import owners_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.treatments_controller import treatment_blueprint
from controllers.pet_types_controller import pet_type_blueprint

# Create the flask app
app = Flask(__name__)

# Set secret-key
app.secret_key = b'2At$svhuBy7X/.c5btxRY67e/s29'

# Register blueprints
app.register_blueprint(pets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(treatment_blueprint)
app.register_blueprint(pet_type_blueprint)

# Default routes
@app.route('/')
def index():
    pets = PR.select_all()
    vets = VR.select_all()
    owners = OR.select_all()
    return render_template('index.html', title='Home', pets=pets, vets=vets, owners=owners)

if (__name__ == '__main__'):
    app.run()
