# Import modules for testing
import unittest
from classes import Pet, Owner, Vet, Note, PetType

# Run tests

class VetsoObjectsTesting(unittest.TestCase):

    def setUp(self):
        # Owner objects
        self.owner_1 = Owner('Ben', 'Davidson', 'ben@ben.com', '0123456789', 'Bla', 'blabla', 'Glasgow', True)
        self.owner_2 = Owner('Becca', 'Kane', 'becca@becca.com', '0123456781', 'Bla', 'blabla', 'Glasgow', True)

        # Vet objects
        self.vet = Vet('John', 'Doe')

        # Pet types
        self.type_1 = PetType('Dog', 'Spaniel')
        self.type_2 = PetType('Cat', 'Turtleshell')

        # Pets
        self.pet_1 = Pet('Stuart', '20-02-20', self.owner_1, self.type_1, self.vet)

    # Define tests
    def test_pet_object_pet_name(self):
        self.assertEqual('Stuart', self.pet_1.name)

    def test_pet_object_owner_name(self):
        self.assertEqual('Ben', self.pet_1.owner.first_name)

# Allow tests to run

if __name__ == "__main__":
    unittest.main()
