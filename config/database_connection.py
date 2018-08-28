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
        from run import APP

        if not APP.config['TESTING']:
            connection = psycopg2.connect(
                """dbname='Stackoverflow-lite' 
                user='akram' 
                host='localhost'\
                password=''
                port='5432'"""

            )
            return connection 
        

