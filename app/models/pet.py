# New class: PET
# This class creates a pet object to be used for displaying data within browser
# REQUIREMENTS: name(STRING), dob (STRING), owner (Owner Object), pet_type(PetType Object), id (INT/None)
# FUNCTIONS: convert_dob_to_text() - returns a string
#          : convert_dob_to_age()  - returns a string
class Pet:
    # Initialise the class
    def __init__(self, name, dob, owner, pet_type, vet, id=None):
        self.name = name
        self.dob = dob
        self.owner = owner
        self.pet_type = pet_type
        self.vet = vet
        self.id = id

    # Class functions
    def convert_dob_to_text(self):
        # This function is used to display the D.O.B with Xth of Month, Year rather than
        # DD/MM/YYYY
        pass

    def convert_dob_to_age(self):
        # This function is used to generate a pets age from its D.O.B
        pass