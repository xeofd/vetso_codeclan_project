-- DROP THE TABLES IF THEY EXIST
DROP TABLE IF EXISTS perscribed_treatment;
DROP TABLE IF EXISTS appointment;
DROP TABLE IF EXISTS note;
DROP TABLE IF EXISTS pet;
DROP TABLE IF EXISTS owner;
DROP TABLE IF EXISTS pet_type;
DROP TABLE IF EXISTS treatment;
DROP TABLE IF EXISTS vet;

-- CREATE TABLES

-- PET TYPES:
-- This table controls the types of animal and breed
-- a pet can be.
CREATE TABLE pet_type(
    id SERIAL PRIMARY KEY NOT NULL,
    type VARCHAR(24) NOT NULL,
    breed VARCHAR(20) NOT NULL
);

-- OWNER:
-- This table controls the data that is held about a pets
-- owner, includes name, address & contact info
CREATE TABLE owner(
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(48) NOT NULL,
    last_name VARCHAR(48) NOT NULL,
    email_address VARCHAR(100),
    contact_number INT,
    address VARCHAR(100) NOT NULL,
    post_code VARCHAR(8),
    city VARCHAR(100),
    registered BOOLEAN NOT NULL
);

-- VET
-- This table holds data about vets who work in the 
-- practice, contains only the vets name ATM.
CREATE TABLE vet(
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(48) NOT NULL,
    last_name VARCHAR(48) NOT NULL
);

-- PET
-- This table controls the data this is held about a pet
-- includes name, type of pet and its owner
CREATE TABLE pet(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(64) NOT NULL,
    dob DATE NOT NULL,
    owner_id INT REFERENCES owner(id) NOT NULL,
    type_id INT REFERENCES pet_type(id) NOT NULL,
    vet_id INT REFERENCES vet(id) NOT NULL
);

-- APPOINTMENTS
-- This table holds data about appointments between vets
-- and pets, it contains a date, pet id and vet id
CREATE TABLE appointment(
    id SERIAL PRIMARY KEY NOT NULL,
    date DATE NOT NULL,
    note TEXT NOT NULL,
    vet_id INT REFERENCES vet(id) NOT NULL,
    pet_id INT REFERENCES pet(id) NOT NULL
);

-- NOTE
-- This table contains notes about treatments and
-- when it was created, along with the pet id and vet id
CREATE TABLE note(
    id SERIAL PRIMARY KEY NOT NULL,
    date DATE NOT NULL,
    note_text TEXT NOT NULL,
    pet_id INT REFERENCES pet(id) NOT NULL,
    vet_id INT REFERENCES vet(id) NOT NULL
);

-- TREATMENT
-- This table contains data about treatments available
-- data includes, name, cost, length of treatment, type
-- and its medicine
CREATE TABLE treatment(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(225) NOT NULL,
    cost FLOAT NOT NULL,
    length INT,
    medicine VARCHAR(225),
    type VARCHAR(20) NOT NULL
);

-- PERSCRIBED_TREATMENTS
-- This table holds data to connect pets and treatments
-- as they have a many to many relationship with each other
CREATE TABLE perscribed_treatment(
    id SERIAL PRIMARY KEY NOT NULL,
    pet_id INT REFERENCES pet(id) NOT NULL,
    treatment_id INT REFERENCES treatment(id) NOT NULL
);