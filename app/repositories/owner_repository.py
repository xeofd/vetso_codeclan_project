# Import required modules
from database.run_sql import run_sql
from models.owner import Owner

# Functions

# FUNCTION: save(item)
# This function is used to save data from a python object to the database
def save(owner):
    # Create the SQL query, pass in data and run it
    sql = "INSERT INTO owner (first_name, last_name, email_address, contact_number, address, post_code, city, registered) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [owner.first_name, owner.last_name, owner.email, owner.contact_number, owner.address, owner.post_code, owner.city, owner.registered]
    result = run_sql(sql, values)

    # Set the object ID to the one generated by the database
    if len(result) > 0:
        id = result[0]['id']
        owner.id = id

    return owner

# FUNCTION: select_all()
# This function is used to select all of the owners from the database and create python objects
# using the data so they can be displayed
def select_all():
    # Create empty list to hold objects
    owners = []

    # Create the SQL query, pass in the data and run
    sql = "SELECT * FROM owner"
    results = run_sql(sql)

    # Loop through the data
    for row in results:
        # Create new owner object and append it to the list
        new_owner = Owner(row['first_name'], row['last_name'], row['email_address'], row['contact_number'], row['address'], row['post_code'], row['city'], row['registered'], row['id'])
        owners.append(new_owner)

    return owners

# FUNCTION: select(item_id)
# This function is used to select a specific owner by the ID in the database to be able to create an object
# that can be displayed
def select(owner_id):
    # Create the SQL query, pass in the data and run it
    sql = "SELECT * FROM owner WHERE id = %s"
    values = [owner_id]
    result = run_sql(sql, values)

    # Create object if data is found in the database
    if len(result) > 0:
        new_owner = Owner(result[0]['first_name'], result[0]['last_name'], result[0]['email_address'], result[0]['contact_number'], result[0]['address'], result[0]['post_code'], result[0]['city'], result[0]['registered'], result[0]['id'])
    
    return new_owner

# FUNCTION: delete(item_id)
# This function is used to delete a specific item from the database using its id
def delete(owner_id):
    # Create the SQL query, pass in the data and run it
    sql = "DELETE FROM owner WHERE id = %s"
    values = [owner_id]
    run_sql(sql, values)

# FUNCTION: update(item_id)
# This function is used to update data within the database
def update(owner):
    # Create SQL query, pass in the data and run it
    sql = "UPDATE owner SET (first_name, last_name, email_address, contact_number, address, post_code, city, registered) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.email, owner.contact_number, owner.address, owner.post_code, owner.city, owner.registered, owner.id]
    run_sql(sql, values)

# FUNCTION: delete_all()
# This function is used to delete all data from the table that coresponds to the class it is run from
def delete_all():
    # Create SQL query and run it
    sql = "DELETE FROM owner"
    run_sql(sql)