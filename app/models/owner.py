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
