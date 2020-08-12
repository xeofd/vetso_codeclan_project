# Import required modules
from database.run_sql import run_sql
from models.appointment import Appointment
from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as PR
import repositories.vet_repository as VR

# CRUD FUNCTIONS

# SAVE
def save(appointment):
    # Create SQL query, insert data and run
    sql = "INSERT INTO appointment (date, note, vet_id, pet_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [appointment.date, appointment.note, appointment.vet.id, appointment.pet.id]
    result = run_sql(sql, values)

    if len(result) > 0:
        # Set objects id to db id
        id = result[0]['id']
        appointment.id = id

    return appointment

# SELECT
def select(id):
    # Create SQL query, insert data and run
    sql = "SELECT * FROM appointment WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    # Check result has returned something
    if len(result) > 0:
        # Grab secondary data
        vet = VR.select(result[0]['vet_id'])
        pet = PR.select(result[0]['pet_id'])

        # Create new object
        appointment = Appointment(result[0]['date'], result[0]['note'], vet, pet, result[0]['id'])

    return appointment

# SELECT ALL
def select_all(id):
    # Create list of appointments == empty list
    appointments = []

    # Create SQL query, pass in data && run
    sql = "SELECT * FROM appointment"
    results = run_sql(sql)

    # Loop through results
    for row in results:
        # Grab secondary data
        vet = VR.select(row['vet_id'])
        pet = PR.select(row['pet_id'])

        # Create new object
        appointment = Appointment(row['date'], row['note'], vet, pet, row['id'])
        appointments.append(appointment)

    return appointments

# DELETE
def delete(id):
    # Create SQL query, pass in data and run
    sql = "DELETE FROM appointment WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE ALL
def delete_all():
    # Create SQL query and run
    sql = "DELETE FROM appointment"
    run_sql(sql)

# SELECT BY PET
def select_by_pet(id):
    # Create list of appointments == empty list
    # Create list of appointments == empty list
    appointments = []

    # Create SQL query, pass in data && run
    sql = "SELECT * FROM appointment WHERE pet_id = %s"
    values = [id]
    results = run_sql(sql, values)

    # Loop through results
    for row in results:
        # Grab secondary data
        vet = VR.select(row['vet_id'])
        pet = PR.select(id)

        # Create new object
        appointment = Appointment(row['date'], row['note'], vet, pet, row['id'])
        appointments.append(appointment)

    return appointments

# SELECT BY VET
def select_by_vet(id):
    # Create list of appointments == empty list
    # Create list of appointments == empty list
    appointments = []

    # Create SQL query, pass in data && run
    sql = "SELECT * FROM appointment WHERE vet_id = %s"
    values = [id]
    results = run_sql(sql, values)

    # Loop through results
    for row in results:
        # Grab secondary data
        vet = VR.select(id)
        pet = PR.select(row['pet_id'])

        # Create new object
        appointment = Appointment(row['date'], row['note'], vet, pet, row['id'])
        appointments.append(appointment)

    return appointments