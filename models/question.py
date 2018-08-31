"""
This module is a ride model with its attributes
"""
from config.db_link import linkdb
import datetime


class Question(object):
    """
    This class represents a question entity
    """

    def __init__(self, *args):
        self.title = args[0]
        self.question = args[1]
        self.user_id = args[2]
        self.question_date = datetime.date.today()[3]
        self.question_time = datetime.datetime.now[4]

    def save_question(self):
        """
        This method saves a question in the database
        """

        question_sql = """INSERT INTO "Questions"( title, question, user_id, question_date, question_time) VALUES(%s,%s, %s,%s,%s);"""
        question_data = (
            self.title,
            self.question, 
            self.user_id,
            self.question_date,
            self.question_time
            )
        linkdb.save(question_sql, question_data)

    def check_question_existance(self):
        """
        This method checks if a question exists already.
       
        """
        sql = """SELECT question_id, title, question
         FROM Questions WHERE title = %s AND question = %s 
        """
        question_data = (self.title, self.question )
        question = linkdb.retrieve_one(sql, question_data)
        if question is None:
            return {"status": "success", "message": "question does not exists"}
        return {"status": "failure", "message": "question already exists"}