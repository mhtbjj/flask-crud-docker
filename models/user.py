import sqlite3

class User:
    def __init__(self, id, username, password):
        print("User Model initialized.")
        self.id = id
        self.username = username
        self.password = password
    

    @classmethod
    def find_by_username(cls, username):
        # Make connection to the DB by providing the path/db_file.db_extension
        connection = sqlite3.connect('data.db')
        # Get Cursor from the cursor
        cursor = connection.cursor()
        # Define Query
        query_by_username = 'SELECT * FROM users WHERE username=?'
        # Execute the query with cursor
        result = cursor.execute(query_by_username, (username,))
        # fetch one row from the returned result set
        row = result.fetchone()
        # If row exist then Initialize the User otherwise None
        if row:
            user = cls(*row)
        else:
            user = None
        # Close the Connection
        connection.close()
        # Logs the value which we are going to return
        print(user)
        # return the user
        return user

    @classmethod
    def find_by_id(cls, _id):
        # Make connection to the DB by providing the path/db_file.db_extension
        connection = sqlite3.connect('data.db')
        # Get Cursor from the cursor
        cursor = connection.cursor()
        # Define Query
        query_by_username = 'SELECT * FROM users WHERE id=?'
        # Execute the query with cursor
        result = cursor.execute(query_by_username, (_id,))
        # fetch one row from the returned result set
        row = result.fetchone()
        # If row exist then Initialize the User otherwise None
        if row:
            user = cls(*row)
        else:
            user = None
        # Close the Connection
        connection.close()
        # Logs the value which we are going to return
        print(user)
        # return the user
        return user
        
    # def find_by_username(self, username):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query_by_username = 'SELECT * FROM users WHERE username=?'
    #     result = cursor.execute(query_by_username, (username,))
    #     row = result.fetchone()
    #     if row:
    #         user = User(row[0], row[1], row[2])
    #     else:
    #         user = None
    #     connection.close()
    #     print(user)
    #     return user

    # def find_by_id(self, _id):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query_by_username = 'SELECT * FROM users WHERE id=?'
    #     result = cursor.execute(query_by_username, (_id,))
    #     row = result.fetchone()
    #     if row:
    #         user = User(row[0], row[1], row[2])
    #     else:
    #         user = None
    #     connection.close()
    #     print(user)
    #     return user