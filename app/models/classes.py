# New class: PET
# This class creates a pet object to be used for displaying data within browser
# REQUIREMENTS: name(STRING), dob (STRING), owner (Owner Object), pet_type(PetType Object), id (INT/None)
# FUNCTIONS: convert_dob_to_text() - returns a string
#          : convert_dob_to_age()  - returns a string
class Pet:
    # Initialise the class
    def __init__(self, name, dob, owner, pet_type, id=None):
        self.name = name
        self.dob = dob
        self.owner = owner
        self.pet_type = pet_type
        self.id = id

    # Class functions
    def convert_dob_to_text(self):
        # This function is used to display the D.O.B with Xth of Month, Year rather than
        # DD/MM/YYYY
        pass

    def convert_dob_to_age(self):
        # This function is used to generate a pets age from its D.O.B
        pass

# New class: OWNER
# This class creates and owner object to be used for displaying data within the browser
# REQUIREMENTS: first_name (STRING), last_name (STRING), email (STRING), contact_number (INT),
#             : address (STRING), post_code (STRING), city (STRING), registered (BOOL), id (INT)
# FUNCTIONS: N/A
class Owner:
    # Initialise the class
    def __init__(self, first_name, last_name, email, contact_number, address, post_code, city, registered, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number
        self.address = address
        self.post_code = post_code
        self.city = city
        self.registered = registered
        self.id = id

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

# New class: NOTE
# This class creates a note object to be used for displaying data within the browser
# REQUIREMENTS: date (STRING), note_text (STRING), pet (OBJECT), vet (OBJECT), id (INT)
# FUNCTIONS: N/A
class Note:
    # Initialise
    def __init__(self, date, note_text, pet, vet, id=None):
        self.date = date
        self.note_text = note_text
        self.pet = pet
        self.vet = vet
        self.id = id