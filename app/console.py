# Import required models
from models.classes import Pet, Owner, PetType, Vet, Note
import repositories.pet_type_repository as PTR
import repositories.owner_repository as OR
import repositories.pet_repository as PR
import repositories.note_repository as NR
import repositories.vet_repository as VR

# Drop the data from the tables
PTR.delete_all()
OR.delete_all()
PR.delete_all()
VR.delete_all()
NR.delete_all()

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

# Pets
pet_1 = Pet('Hudini', '1/1/2012', owner_1, pet_type_3)
PR.save(pet_1)

pet_2 = Pet('KitKat', '1/1/2010', owner_1, pet_type_3)
PR.save(pet_2)

