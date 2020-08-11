# New class: PET TYPE
# This class creates an object to be used to help create a Pet object
# REQUIREMENTS: animal_type (STRING), breed (STRING), id (INT)
# FUNCTIONS: N/A
class PetType:
    # Initialise the function
    def __init__(self, animal_type, breed, id=None):
        self.type = animal_type
        self.breed = breed
        self.id = id