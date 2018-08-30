from flask import jsonify, request
from api.config.db_link import linkdb
from api.models.questions import GetAllquestion
#from api.models.error_messages import ErrorMessage


class AnswerModel(object):
    """
    This class contains methods that handles answers posted on a specific question
    """

    #error_message = ErrorMessage()

    sql = """ SELECT "users".user_name,
            "questions".user_id, answer.* FROM answers JOIN "user" ON("answers".user_id = "users".user_id)\
            JOIN "questions" ON("answers".question_id = "questions".question_id) JOIN "user" t1\
            ON(t1.user_id = "questions".user_id)"""

    def return_all_requests(self, question_id=None, user_id=None):
        """
        This method returns all answers posted on a question
        :return
        """
        confirm_id = None
        answer_sql = None
        answer_data = None

        if user_id:
            confirm_id = linkdb.retrieve_one(
                """SELECT "user_id" FROM "users" WHERE "user_id" = %s""",
                (user_id, ))
            answer_sql = answer_sql = self.sql + """ WHERE "answer".user_id = %s"""
            answer_data = (user_id, )
        else:
            confirm_id = linkdb.retrieve_one(
                """SELECT "question_id" FROM "questions" WHERE "question_id" = %s""",
                (question_id, ))
            answer_sql = self.sql + """ WHERE "answer".question_id = %s"""
            answer_data = (question_id, )

        if confirm_id:
            answers_turple_list = linkdb.retrieve_all(answer_sql, answer_data)
            answer_list = []
            for answer_tuple in answers_turple_list:
                answer_dict = {
                    "username": request_tuple[0],
                    "answer_id": request_tuple[1],
                    "user_id": request_tuple[2],
                    "question_id": request_tuple[3],
                }
                answer_list.append(answer_dict)

            return jsonify({"message": "Answer retrieved successfully",
                            "answers": answer_list}), 200
        if user_id:
            GetAllquestion.no_user_found_response("No answers found", user_id)
        return self.error_message.no_question_available(questions_id)