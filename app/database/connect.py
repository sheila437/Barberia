import os

import mysql.connector

# Initialize a variable to hold the database connection
connection = None

def connect():
    global connection
    try:
        # Attempt to establish a connection to the MySQL database using environment variables
        connection = mysql.connector.connect(
            host=os.getenv('HOST'), 
            port=int(os.getenv('PORT')),
            database=os.getenv('DATABASE'),
            user=os.getenv('USERDB'),
            password=os.getenv('PASSWORD')
        )
        
        # Check if the connection is successfully established
        if connection.is_connected():
            print('Connected to MySQL database')

    except mysql.connector.Error as e:
        # Print an error message if a connection error occurs
        print(e)
