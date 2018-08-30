"""
 This module handles the database connection
"""
import os
import psycopg2

class Databaseconn(object):
    """
    This Class contains methods that connects to the database 
    """
    @staticmethod
    def database_connection():
        """
        This method creates a connection to the databse
        "dbname='mydb' user='mydb1' host='localhost' password='mydb123' port='5432'"
        :retun: connection
        """
        #from run import APP

        # if APP.config['TESTING']:
        connection = psycopg2.connect("""dbname='stackoverflow' user='akram'  host='localhost'  password='12345'  port='5432'""" )
        return connection
        
    @staticmethod
    def create_tables():
        """
        This method creates tables in the PostgreSQL database.
        It connects to the database and creates tables one by one
        for command in commands:
        cur.execute(command)
        """
        connection = psycopg2.connect("""dbname='stackoverflow' user='akram'  host='localhost'  password='12345'  port='5432' """ )
        commands = (
            """
            CREATE TABLE if not exists "users" (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(80) NOT NULL
                    
                )
            """,
            """
            CREATE TABLE if not exists "Questions" (
                    question_id SERIAL PRIMARY KEY,
                    title VARCHAR (50) NOT NULL,
                    question VARCHAR(255) NOT NULL,
                    date DATE,
                    time TIME
                    
                )
            """,
            """
            CREATE TABLE if not exists "answers" (
                    answer_id SERIAL PRIMARY KEY,
                    answer VARCHAR(50) NOT NULL
                   
                )
            """,)

        try:

            cur = connection.cursor()
            for command in commands:
                cur.execute(command)
            connection.commit()
            cur.close()
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()

db = Databaseconn()
# Databaseconn.database_connection() 
db.create_tables()
