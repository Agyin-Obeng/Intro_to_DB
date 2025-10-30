#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database in MySQL.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection if open
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            # Connection failed before being established
            pass

if __name__ == "__main__":
    create_database()
