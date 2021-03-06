# Import required modules
from database.run_sql import run_sql
from models.pet_type import PetType

# CRUD FUNCTIONS

# FUNCTION: save(item)
# This function is used to save a pet type to the database
def save(pet_type):
    # Create the SQL query && input data before running it
    sql = "INSERT INTO pet_type (type, breed) VALUES (%s, %s) RETURNING id"
    values = [pet_type.type, pet_type.breed]
    result = run_sql(sql, values)

    # Set the pet objects ID to the ID generated by the database
    pet_type.id = result[0]['id']
    return pet_type

# FUNCTION: select_all()
# This function is used to select all of the pet types from the database and create python objects
# using the data so they can be displayed
def select_all():
    # Create list of pet objects and set == empty list
    pet_types = []

    # Create the SQL query && input data before running it
    sql = "SELECT * FROM pet_type"
    results = run_sql(sql)

    # Loop through all the results and append the objects to a list
    for row in results:
        # Create new pet type and append it to the list
        new_pet_type = PetType(row['type'], row['breed'], row['id'])
        pet_types.append(new_pet_type)

    return pet_types

# FUNCTION: select(item_id)
# This function is used to select a specific pet type by its ID in the database to be able to create an object
# that can be passed into the Pets object
def select(type_id):
    # Create the SQL query, pass in the data and run it
    sql = "SELECT * FROM pet_type WHERE id = %s"
    values = [type_id]
    result = run_sql(sql, values)

    # Create object if data is found in the database
    if len(result) > 0:
        pet_type = PetType(result[0]['type'], result[0]['breed'], result[0]['id'])
    
    return pet_type

# FUNCTION: delete(item_id)
# This function is used to delete a specific item from the database using its id
def delete(type_id):
    # Create the SQL query, pass in the data and run it
    sql = "DELETE FROM pet_type WHERE id = %s"
    values = [type_id]
    run_sql(sql, values)

# FUNCTION: update(item_id)
# This function is used to update data within the database
def update(pet_type):
    # Create SQL query, pass in the data and run it
    sql = "UPDATE pet_type SET (type, breed) = (%s, %s) WHERE id = %s"
    values = [pet_type.type, pet_type.breed, pet_type.id]
    run_sql(sql, values)

# FUNCTION: delete_all()
# This function is used to delete all data from the table that coresponds to the class it is run from
def delete_all():
    # Create SQL query and run it
    sql = "DELETE FROM pet_type"
    run_sql(sql)