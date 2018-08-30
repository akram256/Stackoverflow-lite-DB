"""
This module is a answer model with its attributes
"""
from config.db_link import linkdb


class Answer(object):
    """
    This class represents a answer entity
    """

    def __init__(self, user_id, question_id, answer_id=None):
        self.user_id = user_id
        self.question_id = question_id
        self.answer_id = asnwer_id

    def save_asnwer(self):
        """
        This method saves an answer provided for a question.
        """

        answer_sql = """INSERT INTO "asnwers"(user_id, question_id)
            VALUES((%s), (%s));"""
        answer_data = (self.user_id, self.question_id)
        linkdb.save(asnwer_sql, answer_data)
        
    def return_answer_information(self):
        """
        This method returns the information of a class.
        """
        
        return {
            "user_id": self.question_id,
            "question_id": self.question_id
        }
