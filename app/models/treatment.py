# New class: TREATMENT
# This class creates a treatment object to be saved to database and to be displayed on website
# REQUIREMENTS: name (STRING), cost (FLOAT), length (INT), medicine (STRING), type (STRING), id (INT)
# FUNCTIONS: N/A
class Treatment:
    # Initialise the function
    def __init__(self, name, cost, length, medicine, treatment_type, id=None):
        self.name = name
        self.cost = cost
        self.length = length
        self.medicine = medicine
        self.type = treatment_type
        self.id = id

# New class: PERSCRIBED_TREATMENT
# This class creates a perscribed_treatment object to be saved to database
# REQUIREMENTS: pet (OBJECT), treatment (OBJECT), id (INT)
# FUNCTIONS: N/A
class PerscribedTreatment:
    # Initialise the function
    def __init__(self, pet, treatment, id):
        self.pet = pet
        self.treatment = treatment
        self.id = id