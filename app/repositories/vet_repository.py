# Import required modules
from database.run_sql import run_sql
from models.vet import Vet

# Functions

# FUNCTION: save(item)
# This function is used to save data from a python object to the database
def save(vet):
    # Create the SQL query, pass in data and run it
    sql = "INSERT INTO vet (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name]
    result = run_sql(sql, values)

    # Set the object ID to the one generated by the database
    if len(result) > 0:
        id = result[0]['id']
        vet.id = id

    return vet

# FUNCTION: select_all()
# This function is used to select all of the vets from the database and create python objects
# using the data so they can be displayed
def select_all():
    # Create empty list to hold objects
    vets = []

    # Create the SQL query, pass in the data and run
    sql = "SELECT * FROM vet"
    results = run_sql(sql)

    # Loop through the data
    for row in results:
        # Create new vet object and append it to the list
        new_vet = Vet(row['first_name'], row['last_name'], row['id'])
        vets.append(new_vet)

    return vets

# FUNCTION: select(item_id)
# This function is used to select a specific vet by the ID in the database to be able to create an object
# that can be displayed
def select(vet_id):
    # Create the SQL query, pass in the data and run it
    sql = "SELECT * FROM vet WHERE id = %s"
    values = [vet_id]
    result = run_sql(sql, values)

    # Create object if data is found in the database
    if len(result) > 0:
        new_vet = Vet(result[0]['first_name'], result[0]['last_name'], result[0]['id'])
    
    return new_vet

# FUNCTION: delete(item_id)
# This function is used to delete a specific item from the database using its id
def delete(vet_id):
    # Create the SQL query, pass in the data and run it
    sql = "DELETE FROM vet WHERE id = %s"
    values = [vet_id]
    run_sql(sql, values)

# FUNCTION: update(item_id)
# This function is used to update data within the database
def update(vet):
    # Create SQL query, pass in the data and run it
    sql = "UPDATE vet SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.id]
    run_sql(sql, values)

# FUNCTION: delete_all()
# This function is used to delete all data from the table that coresponds to the class it is run from
def delete_all():
    # Create SQL query and run it
    sql = "DELETE FROM vet"
    run_sql(sql)