from mysql.connector import connect, Error
from config import DB_NAME, DB_PASS, DB_USER, HOST

class DbConnectionError(Error):
    pass

def get_connection():
    try:
        connection = connect(
            host=HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        print(f"Connection Established: {DB_NAME}")
        return connection
    
    except Error as err:
        raise DbConnectionError(f"Unable To Establish Connection: {err}")