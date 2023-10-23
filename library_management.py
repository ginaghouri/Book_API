from db_connection import get_connection, Error, DbConnectionError

def get_books():
    try:
        with get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                SELECT * FROM books
                """)
                result = cursor.fetchall()
                print(result)
                return result
    except Error as err:
        raise DbConnectionError(f"Unable To Read DB: {err}")

def add_new_book(bookData):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO books (name, author, pages, publication_date)"""
"""VALUES (%s, %s, %s, %s)
                """, [bookData['name'], bookData['author'], bookData['pages'], bookData['publication_date']])
                connection.commit()
                print("Book Added!")
    except Error as err:
        raise DbConnectionError(f"Unable to Write to DB: {err}")

def update_book_data(id, data):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                for key in data:
                    query = f"UPDATE books SET {key} = %s WHERE id = %s"
                    cursor.execute(query, [data[key], id])

                    connection.commit()
                    print(f"Record '{key}' updated for book id {id}")

    except Error as err:
        raise DbConnectionError(f"Failed to Update record: {err}")

def delete_book_record(id):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                DELETE FROM books
                WHERE id = %s
                """, [id])
                connection.commit()
                print(f"Record Deleted!: {id}")
    except Error as err:
        raise DbConnectionError(f"Unable To Delete Record: {err}")

def get_a_book(id):
    try:
        with get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                SELECT * FROM books
                WHERE id = %s
                """, [id])
                result = cursor.fetchall()
                return result
    except Error as err:
        raise DbConnectionError(f"Unable To Read Record: {err}")
