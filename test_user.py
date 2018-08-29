"""
This module contains tests for user account creatiom
and signing in.
"""
import uuid
from unittest import TestCase
from flask import json
import psycopg2
from models.user import User
from run import APP
from models.database_connection import Databaseconn


class TestUserAuthTestCase(TestCase):
    """
    Tests run for the api end pints.
    """
    user1 = User("akram",
                 "akram@gmail.com",  "222")
    empty_user = User( "",
                       "akram.com",  "45")
    def setUp(self):
        """
        Define test variables and initialize app.
        """
        APP.config['TESTING'] = True
        self.app = APP

    def test_app_is_development(self):
        """
        This method tests configuration variables such that they are set correctly
        """
        self.assertNotEqual(APP.config['SECRET_KEY'], "my-key")
        self.assertTrue(APP.config['DEBUG'] is True)
        self.assertTrue(APP.config['TESTING'] is True)

    def test_user_registration(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        response = self.client().post('/api/v1/auth/signup/', data=json.dumps(
            self.user1.__dict__), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.content_type == 'application/json')
        self.assertIn("user", response.json)
        self.assertEqual("Successfully registered", response.json['message'])
        self.assertTrue(response.json['user'])

    def test_content_type_not_json(self):
        """
        Test that the content type that is not application/json
        returns an error message
        :return:
        """
        response = self.client().post('/api/v1/auth/signup/', data=json.dumps(
            self.user1.__dict__), content_type='text/plain')

        self.assertEqual(response.status_code, 400)
        self.assertEqual("Failed Content-type must be json", response.json['error_message'])

    def test_empty_attributes_not_sent(self):
        """
        This method tests that data is not sent with empty fields
        """
        response = self.client().post('/api/v1/auth/signup/', data=json.dumps(
            self.empty_user.__dict__), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.json)
        self.assertEqual("Some fields are not defined", response.json['error_message'])

    def test_partial_fields_not_sent(self):
        """
        This method tests that data with partial fields is not send
        on registering
        """
        response = self.client().post('/api/v1/auth/signup/', data=json.dumps(
            dict(username=self.user1.username, email=self.user1.email)),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual("Some fields are missing, all fields are required",
                         response.json['error_message'])

    def test_user_login(self):
        """
        Test for login of a registered user
        """
        self.client().post('/api/v1/auth/signup/', data=json.dumps(
            self.user1.__dict__), content_type='application/json')

        response = self.client().post(
            '/api/v1/auth/login/',
            data=json.dumps(dict(
                email_address=self.user1.email,
                password=self.user1.password
            )),
            content_type='application/json'
        )

        self.assertTrue(response.json['status'] == 'success')
        self.assertTrue(response.json['message'] == 'Successfully logged in.')
        self.assertTrue(response.json['auth_token'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 200)

   