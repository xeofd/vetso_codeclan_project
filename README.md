# Vetso - CodeClan Python Project ##

This is my first project for CodeClan. The project is a simple website with a Python & postgreSQL backend for a vets so they can keep track of pets, vets and owners.

## Required software to run

This project requires **Python**, **postgreSQL**, **Flask** and **Psycopg2** to work properly.

## Set up the site

Step one is to create a psql database:

```SQL
CREATE DATABASE vetso;
```

Step two is to create the tables for the database:

```SH
> cd app
> psql -d vetso -f database/db.sql
```

Step three is to run flask to get the site online:

```SH
> cd app
> flask run
```
Once you have finished these three steps you should have a working version of the app.

A final optional step is to run the python console to input some sample data:

```SH
> cd app
> python3 console.py
```