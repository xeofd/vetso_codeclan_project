# Imports
from datetime import datetime

# New class: APPOINTMENTS
# This class creates an appointment object that can be used to save data to db and to display data
# REQUIREMENTS: date (STRING), note (STRING) vet (OBJECT), pet (OBJECT), id (INT)
# FUNCTIONS: days_unit()
class Appointment:
    # Initialise the class
    def __init__(self, date, note, vet, pet, id=None):
        self.date = date
        self.note = note
        self.vet = vet
        self.pet = pet
        self.days_until_count = 0
        self.id = id

    # Functions
    def days_until(self):
        # Find current date and split into int
        current_date = datetime.today()
        current_date = current_date.strftime('%Y%m%d')
        current_date = int(current_date)

        # Split appointment date into int
        appointment_date = str(self.date).split('-')
        appointment_date = appointment_date[0] + appointment_date[1] + appointment_date[2]
        appointment_date = int(appointment_date)

        # Check where appointment date is compaired to current date
        if appointment_date == current_date:
            self.days_until_count = 0
        elif appointment_date < current_date:
            self.days_until_count = -1
        else:
            self.days_until_count = appointment_date - current_date