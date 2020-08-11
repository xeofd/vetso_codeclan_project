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