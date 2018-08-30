# Stackoverflow-lite-DB
Stackoverflow-lite is a question answering application that provides user with the ability to Post a question  and answers are provided for that question.

**Features**

    - Register a user
    - Login a user 
    - Get all questions 
    - Get a questions
    - Post a question
    - Post answer to a question
    -Delete a question
    -Mark an answer as preferred
    
**API end points**

- POST /api/v1/auth/signup 
- POST /api/v1/auth/login 
- GET /api/v1/questions 
- GET /api/v1/questions/`<question_Id>`
- POST /api/v1/questions
- POST /api/v1/questions/`<question_Id>`/answers-

**Getting Started**

These instructions will enable you to run the project on your local machine.

**Prerequisites**

Below are the things you need to get the project up and running.

- git : To update and clone the repository
- python2.7 or python3: Language used to develop the api
- pip: A python package used to install project requirements specified in the requirements text file.

**Installing the project**

Type: 
        
        "git clone https://github.com/akram256/Stackoverflow-lite-DB.git"
   in the terminal or git bash or command prompt.

To install the requirements. run:

      pip install -r requirements.txt

cd to the folder Stackoverflow-lite-DB
And from the root of the folder, type:
      
      python run.py
      
To run the tests and coverage, from the root folder, type: 
        
        pytest --cov=api/
