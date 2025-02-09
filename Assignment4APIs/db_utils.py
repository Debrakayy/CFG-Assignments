import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return connection


def get_all_records(): # retrieve all records from the 'users'
    privacy_db = 'tests'
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM users"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")


    finally:

        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def execute_user(new_user_dict):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = f"""
         INSERT INTO users (name, email, request_type, request_status)
         VALUES ('{new_user_dict['name']}', '{new_user_dict['email']}', {new_user_dict['request_type']}, {new_user_dict.get['request_status','PENDING']})
         """

        # Execute the query
        cur.execute(query)

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        print("User added successfully!")

        query = """SELECT * FROM users"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def delete_users_by_id(user_id):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        del_query = """DELETE FROM students WHERE student_id = {}""".format(user_id)
        cur.execute(del_query)

        db_connection.commit()  # IMPORTANT!!! Commit the transaction to apply the deletion

        # you can leave little messages for yourself and debugging like this
        print(f"Record with user_id {user_id} deleted successfully.")


        select_query = "SELECT * FROM students"
        cur.execute(select_query)
        remaining_records = cur.fetchall()  # Get all remaining records
        cur.close()

        return remaining_records


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    print("TESTING DB CONNECTION")
    print(get_all_records())

