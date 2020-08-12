# Import required models
import pdb

from models.pet import Pet
from models.pet_type import PetType
from models.treatment import Treatment, PerscribedTreatment
from models.vet import Vet
from models.owner import Owner
from models.note import Note
from models.appointment import Appointment
import repositories.pet_type_repository as PTR
import repositories.owner_repository as OR
import repositories.pet_repository as PR
import repositories.note_repository as NR
import repositories.vet_repository as VR
import repositories.perscribed_treatments_repository as perscribed
import repositories.treatment_repository as TR
import repositories.appointment_repository as AR

# Drop the data from the tables
NR.delete_all()
PR.delete_all()
PTR.delete_all()
perscribed.delete_all()
OR.delete_all()
VR.delete_all()
TR.delete_all()

# Create data

# Pet Types
pet_type_1 = PetType('Dog', 'Spaniel')
PTR.save(pet_type_1)

pet_type_2 = PetType('Dog', 'Boarder Collie')
PTR.save(pet_type_2)

pet_type_3 = PetType('Cat', 'Scottish Fold')
PTR.save(pet_type_3)

pet_type_4 = PetType('Horse', 'Clydesdale')
PTR.save(pet_type_4)

pet_type_5 = PetType('Lizard', 'Geko')
PTR.save(pet_type_5)

# Owners
owner_1 = Owner('Ben', 'Davidson', 'example@example.com', 1234567890, '1 Example Drive', 'AB1 2AB', 'Glasgow', True)
OR.save(owner_1)

owner_2 = Owner('Jane', 'Doe', 'example@example.com', 1234567890, '1 Example Drive', 'AB1 2AB', 'Glasgow', True)
OR.save(owner_2)

owner_3 = Owner('John', 'Doe', 'example@example.com', 1234567890, '1 Example Drive', 'AB1 2AB', 'Glasgow', True)
OR.save(owner_3)

# Vets

vet_1 = Vet('John', 'Doe')
VR.save(vet_1)

vet_2 = Vet('Jane', 'Doe')
VR.save(vet_2)

# Pets
pet_1 = Pet('Hudini', '1/1/2012', owner_1, pet_type_3, vet_1)
PR.save(pet_1)

pet_2 = Pet('KitKat', '1/1/2010', owner_1, pet_type_3, vet_1)
PR.save(pet_2)

pet_3 = Pet('Steven', '03/10/2004', owner_3, pet_type_5, vet_2)
PR.save(pet_3)

# Notes

note_1 = Note('09/08/2020', 'Hudini is a stinky boy', pet_1, vet_1)
NR.save(note_1)

# Treatments
treatment_1 = Treatment('Worming tablets', 10, 2, 'dewormitroxin', 'Liquid Spray')
TR.save(treatment_1)

treatment_2 = Treatment('Antibiotics - Stinkyitus', 50, 7, 'stinkicillin', 'Tablet')
TR.save(treatment_2)

# Test appointment

appointment1 = Appointment('2020-09-12', 'Note text', vet_1, pet_3)
AR.save(appointment1)

pdb.set_trace()