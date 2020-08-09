# Import required modules
from flask import Flask, Blueprint, render_template
import repositories.pet_repository as PR
import repositories.vet_repository as VR
import repositories.owner_repository as OR
from controllers.pets_controller import pets_blueprint

# Create the flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(pets_blueprint)

# Default routes
@app.route('/')
def index():
    pets = PR.select_all()
    vets = VR.select_all()
    owners = OR.select_all()
    return render_template('index.html', title='Home', pets=pets, vets=vets, owners=owners)

if (__name__ == '__main__'):
    app.run()
