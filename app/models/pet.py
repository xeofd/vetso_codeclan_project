# Imports
from datetime import datetime

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
        self.age = 0
        self.id = id

    # Class functions
    def convert_dob_to_text(self):
        # This function is used to display the D.O.B with Xth of Month, Year rather than
        # DD/MM/YYYY
        date_split = str(self.dob).split('-')

        # Find day type
        if date_split[2] == '01' or date_split[2] == '21' or date_split[2] == '31':
            day_type = 'st'
        elif date_split[2] == '02' or date_split[2] == '22':
            day_type = 'nd'
        elif date_split[2] == '03' or date_split[2] == '23':
            day_type = 'rd'
        else:
            day_type = 'th'

        # Find month
        if date_split[1] == '01':
            month = 'January'
        elif date_split[1] == '02':
            month = 'Febuary'
        elif date_split[1] == '03':
            month = 'March'
        elif date_split[1] == '04':
            month = 'April'
        elif date_split[1] == '05':
            month = 'May'
        elif date_split[1] == '06':
            month = 'June'
        elif date_split[1] == '07':
            month = 'July'
        elif date_split[1] == '08':
            month = 'August'
        elif date_split[1] == '09':
            month = 'Spetember'
        elif date_split[1] == '10':
            month = 'October'
        elif date_split[1] == '11':
            month = 'November'
        elif date_split[1] == '12':
            month = 'December'

        # Create string and return
        return date_split[2] + day_type + ' ' + month + ' ' + date_split[0]

    def convert_dob_to_age(self):
        # This function is used to generate a pets age from its D.O.B
        current_date = datetime.today()

        # Split the dates to get year
        current_date = current_date.strftime('%Y-%m-%d')
        current_date = current_date.split('-')

        pet_dob = str(self.dob).split('-')

        current_year = int(current_date[0])
        dob_year = int(pet_dob[0])
        
        self.age = current_year - dob_year