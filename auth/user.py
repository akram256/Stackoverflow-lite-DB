"""
This module is a user with its attributes
"""
import datetime
import jwt
from flask import jsonify
from config.db_link import linkdb
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity



class User(object):
    """
    This class represents a User entity
    """
    def __init__(self, *args):
        self.username = args[0]
        self.email= args[1]
        self.password = args[2]

    def save_user(self):
        """
        This method saves a user instance in the database.
        """
        user_data = (self.username, self.email, self.password)
        user_sql = """INSERT INTO "users"(username, email, password)
            VALUES(%s, %s, %s);"""
        linkdb.save(user_sql, user_data)

    def return_user_details(self):
        """
        This method returns the details of the user
        in json format.
        """ 
        return {
            "username": self.username,
            "email": self.email,
        }

    @staticmethod
    def encode_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
      
        try:
            # token = jwt.encode({"user_id": str(user_id),
            #                     "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},
            #                    "APP.secret_key")  
            token = create_access_token( identity = user_id)                    
            return token
        except Exception as error:
            raise error

    @staticmethod
    def decode_token(auth_token):
        """
        Decodes the auth token and returns the user public id
        :param auth_token:
        :return:
        """
        return get_jwt_identity()
        # try:

        #     token = jwt.decode(auth_token)
        #     return {"user_id": token["user_id"],
        #             "state": "Success"}
        # except jwt.ExpiredSignatureError:
        #     return {"error_message": "Signature expired. Please log in again buddy.",
        #             "state": "Failure"}
        # except jwt.InvalidTokenError:
        #     return {"error_message": "Invalid token. Hello, Please log in again buddy.",
        #             "state": "Failure"}

    @staticmethod
    def decode_failure(message):
        """
        This method returns an error message when an error is
        encounterd on decoding the token
        """
        return jsonify({"message": message}), 401

    @staticmethod
    def check_login_status(user_id):
        """
        This method checks whether a user is logged in or not
        If a user is logged in, it returns true and returns
        false if a user is not logged in
        :param user_id: User Id
        :return
        """
        is_loggedin = linkdb.retrieve_one(
            """SELECT "is_loggedin" FROM "users" WHERE "user_id" = %s""",
            (user_id, ))
        if is_loggedin[0]:
            return True
        return False
