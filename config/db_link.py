"""
This module is responsible for database.
"""
import psycopg2
from config.database_connection import Databaseconn


class linkdb(object):
    """
    This class is responsible for making different database
    transactions.
    - inserting data into the database tables
    - updating the data in the database tables
    - quering data in the database tables
    """

    @staticmethod
    def save(sql, data):
        """
        This method inserts the data into the database depending on the
        recieved sql command and the data.
        :param:sql
        :param:data
        """
        connection= Databaseconn.database_connection()
        try:
            cur = connection.cursor()
            cur.execute(sql, data)
            connection.commit()
            cur.close()
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is False:
                connection.close()

    @staticmethod
    def retrieve_one(sql, data):
        """
        This method gets a single row from the database depending on the
        recieved sql command and the data.
        returns the row
        :param:sql
        :param:data
        :return:row
        """
        connection = Databaseconn.database_connection()
        try:
            
            cur = connection.cursor()
            cur.execute(sql, data)
            row = cur.fetchone()
            cur.close()

            if row and not "":
                return row
            return None

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
    @staticmethod
    def retrieve_all(sql, data=None):
        """
        This method gets all rows from the database depending on the
        recieved sql command and the data.
        returns the row
        :param:sql
        :param:data
        :return:row
        """
        list_tuple = []
        connection= Databaseconn.database_connection()
        try:
            connection = Databaseconn.database_connection()
            cur = connection.cursor()
            if data is not None:
                cur.execute(sql, data)
            else:
                cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                list_tuple.append(row)
            cur.close()
            return list_tuple
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is False:
                connection.close()

    @staticmethod
    def edit(sql, data):
        """
        This method edits the data into the database depending on the
        recieved sql command and the data.
        :param:sql
        :param:data
        """
        connection = Databaseconn.database_connection()
        try:
            
            cur = connection.cursor()
            cur.execute(sql, data)
            #updated_rows = cur.rowcount
            connection.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
        #return updated_rows
                