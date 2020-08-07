# Import required modules
from flask import Flask, render_template

# Create the flask app
app = Flask(__name__)

# Register blueprints

# Default routes
@app.route('/')
def index():
    return render_template('index.html', title='Home')

if (__name__ == '__main__'):
    app.run()
