# New class: VET
# This class creates a vet object to be used for displaying data within the browser
# REQUIREMENTS:  first_name (STRING), last_name (STRING), id (INT)
# FUNCTIONS: N/A
class Vet:
    # Initialise the class
    def __init__(self, first_name, last_name, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id