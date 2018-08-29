"""
This module is a ride model with its attributes
"""
from config.db_link import linkdb


class Question(object):
    """
    This class represents a question entity
    """

    def __init__(self, *args):
        self.question_id = args[0]
        self.title = args[1]
        self.question = args[2]
        self.question_date = args[3]
        self.question_time = args[4]

    def save_question(self):
        """
        This method saves a question in the database
        """

        question_sql = """INSERT INTO "questions"(question_id, title, question
            )
        VALUES((%s), %s, %s, %s, %s);"""
        question_data = (
            self.question_id, self.title,
            self.question, self.question_date,
            self.question_time
            )
        linkdb.save(question_sql, question_data)

    def check_question_existance(self):
        """
        This method checks if a question exists already.
       
        """
        sql = """SELECT "question_id", "title", "question"
         FROM "question" WHERE "question_id" = %s
        AND "title" = %s AND "question" = %s 
        """
        question_data = (self.question_id, self.title, self.question )
        question = linkdb.retrieve_one(sql, question_data)
        if question is None:
            return {"status": "success", "message": "question does not exists"}
        return {"status": "failure", "message": "question already exists"}