# Import required modules
from database.run_sql import run_sql
from models.pet import Pet
from models.owner import Owner
from models.pet_type import PetType
from models.vet import Vet
import repositories.pet_type_repository as PTR
import repositories.owner_repository as OR
import repositories.vet_repository as VR

# CRUD FUNCTIONS

# FUNCTION: save(item)
# This function is used to save a pet to the database
def save(pet):
    # Create the SQL query && input data before running it
    sql = "INSERT INTO pet (name, dob, owner_id, type_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.owner.id, pet.pet_type.id, pet.vet.id]
    result = run_sql(sql, values)

    # Set the pet objects ID to the ID generated by the database
    if len(result) > 0:
        id = result[0]['id']
        pet.id = id

    return pet

# FUNCTION: select_all()
# This function is used to select all of the pets from the database and create python objects
# using the data so they can be displayed
def select_all():
    # Create list of pet objects and set == empty list
    pets = []

    # Create the SQL query && input data before running it
    sql = "SELECT * FROM pet"
    results = run_sql(sql)

    # Loop through all the results and append the objects to a list
    for row in results:
        # Get the objects to create the pet object
        pet_type = PTR.select(row['type_id'])
        owner = OR.select(row['owner_id'])
        vet = VR.select(row['vet_id'])

        # Create new pet object && append to pets list
        new_pet = Pet(row['name'], row['dob'], owner, pet_type, vet, row['id'])
        pets.append(new_pet)

    return pets

# FUNCTION: select(item_id)
# This function is used to select a specific pet by its ID in the database to be able to create an object
# that can be displayed
def select(pet_id):
    # Create the SQL query, pass in the data and run it
    sql = "SELECT * FROM pet WHERE id = %s"
    values = [pet_id]
    result = run_sql(sql, values)

    # Create object if data is found in the database
    if len(result) > 0:
        pet_type = PTR.select(result[0]['type_id'])
        owner = OR.select(result[0]['owner_id'])
        vet = VR.select(result[0]['vet_id'])
        new_pet = Pet(result[0]['name'], result[0]['dob'], owner, pet_type, vet, result[0]['id'])
    
    return new_pet

# FUNCTION: delete(item_id)
# This function is used to delete a specific item from the database using its id
def delete(pet_id):
    # Create the SQL query, pass in the data and run it
    sql = "DELETE FROM pet WHERE id = %s"
    values = [pet_id]
    run_sql(sql, values)

# FUNCTION: delete_all()
# This function is used to delete all data from the table that coresponds to the class it is run from
def delete_all():
    # Create SQL query and run it
    sql = "DELETE FROM pet"
    run_sql(sql)

# FUNCTION: update(item_id)
# This function is used to update data within the database
def update(pet):
    # Create SQL query, pass in the data and run it
    sql = "UPDATE pet SET (name, dob, owner_id, type_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.owner.id, pet.pet_type.id, pet.vet.id, pet.id]
    run_sql(sql, values)

# FUNCTION: select_by_owner(item_id)
# This function is used to select all pets by an owner id
def select_by_owner(owner_id):
    # Create list of pets == empty list
    pets = []

    # Create SQL query, input data && run
    sql = "SELECT * FROM pet WHERE owner_id = %s"
    values = [owner_id]
    results = run_sql(sql, values)

    # Loop through the results
    for row in results:
        # Get the objects to create the pet object
        pet_type = PTR.select(row['type_id'])
        owner = OR.select(row['owner_id'])
        vet = VR.select(row['vet_id'])

        # Create new pet object && append to pets list
        new_pet = Pet(row['name'], row['dob'], owner, pet_type, vet, row['id'])
        pets.append(new_pet)

    return pets

# FUNCTION: select_by_vet(item_id)
# This function is used to select all pets by the vet id
def select_by_vet(vet_id):
    # Create list of pets == empty list
    pets = []

    # Create SQL query, input data && run
    sql = "SELECT * FROM pet WHERE vet_id = %s"
    values = [vet_id]
    results = run_sql(sql, values)

    # Loop through the results
    for row in results:
        # Get the objects to create the pet object
        pet_type = PTR.select(row['type_id'])
        owner = OR.select(row['owner_id'])
        vet = VR.select(row['vet_id'])

        # Create new pet object && append to pets list
        new_pet = Pet(row['name'], row['dob'], owner, pet_type, vet, row['id'])
        pets.append(new_pet)

    return pets