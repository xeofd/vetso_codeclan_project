# Import required modules
import psycopg2
import psycopg2.extras as ext

# Functions
def run_sql(sql, values=None):
    # Set variables
    connection = None
    results = []

    # Start try/catch/finally
    try:
        connection = psycopg2.connect("dbname='vetso'")
        cursor = connection.cursor(cursor_factory=ext.DictCursor)
        cursor.execute(sql, values)
        connection.commit()
        results = cursor.fetchall()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    
    return results