# Import required models
from models.classes import Pet, Owner, PetType, Vet, Note
import repositories.pet_type_repository as PTR
import repositories.owner_repository as OR
import repositories.pet_repository as PR
import repositories.note_repository as NR
import repositories.vet_repository as VR

# Create data
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