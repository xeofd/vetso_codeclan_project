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
        self.pet_2 = Pet('Holly', '20-02-20', self.owner_1, self.type_2, self.vet)
        self.pet_3 = Pet('Bran', '20-02-20', self.owner_2, self.type_1, self.vet)

    # Define tests
    def test_pet_object_pet_name(self):
        self.assertEqual('Stuart', self.pet_1.name)

    def test_pet_object_owner_name(self):
        self.assertEqual('Ben', self.pet_1.owner.first_name)

    def test_pet_object_type_breed(self):
        self.assertEqual('Turtleshell', self.pet_2.pet_type.breed)

    def test_owner_object_email(self):
        self.assertEqual('ben@ben.com', self.owner_1.email)

    def test_owner_object_contact_number(self):
        self.assertEqual('0123456781', self.owner_2.contact_number)

# Allow tests to run

if __name__ == "__main__":
    unittest.main()
