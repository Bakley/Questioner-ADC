# Questioner-ADC

[![Maintainability](https://api.codeclimate.com/v1/badges/327b489ebb4d383d38c6/maintainability)](https://codeclimate.com/github/Bakley/Questioner-ADC/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0c82cd66a38040928a1cdcf0e8044a75)](https://www.codacy.com/app/Bakley/Questioner-ADC?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bakley/Questioner-ADC&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/Bakley/Questioner-ADC/badge.svg?branch=develop)](https://coveralls.io/github/Bakley/Questioner-ADC?branch=develop)
[![Build Status](https://travis-ci.org/Bakley/Questioner-ADC.svg?branch=develop)](https://travis-ci.org/Bakley/Questioner-ADC)

Crowd-source questions for a meetup. Building a set of API endpoints where the users can vote on asked questions and they bubble to the top or bottom of the log.

# Required Features
1. Admin can create meet ups.
2. Users can create an account and log in.
3. Users can post questions to a specific meet up.
4. Users can up vote or down vote a question.
5. Questions are sorted based on the number of up votes a question has, which helps the meet up organizer(s) to prioritize questions most users are interested in.
6. Users can post comments to a specific question.

## API Endpoints covered included in this branch


| Method        |       Endpoint                              |         Description                           |
| ------------- |       -------------                         |         -------------                         |
| `GET`         | `/api/v1/meetups/upcoming`                  |   Gets all meetups records                    |
| `GET`         | `/api/v1/meetups/<meetup-id>`               |   Get a specific meetup record                |
| `POST`        | `/api/v1/meetups`                           |   Create a meetup record                      |
| `POST`        | `/api/v1/questions`                         |   Create a question record                    |
| `POST`        | `/api/v1/users/registration`                |   Register a user                             |
| `POST`        | `/api/v1/users/login`                       |   Sign in a User                              |
| `POST`        | `/api/v1/meetups/<meetup-id/rsvps>`         |   User respond to a meetup                    |
| `PATCH`       | `/api/v1/questions/<questions-id>/upvote`   |   vote on a meetup question                   |
| `PATCH`       | `/api/v1/questions/<questions-id/downvote`  |   vote on a meetup question                   |



# Setting up your system

Make sure you already have Python3, Pip and Virtualenv installed in your system.

# How to get started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir Questioner-ADC
```

Afterwhich we go into the directory:

```
cd Questioner-ADC
```

## Create a Python Virtual Environment for our Project

Since we are using Python 3, create a virtual environment by typing:

```
virtualenv -p python3 venv
```

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:

```
source venv/bin/activate
```

## Clone and Configure a Flask Project

Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:

```
git clone https://github.com/Bakley/Questioner-ADC.git
```

Next, install the requirements by typing:

```
pip install -r requirements.txt
```

## How to run the app

### Scenario 1

Install dotenv file

```
pip install -U python-dotenv
```

We add the new package to the requirements file.

```
pip freeze > requirements.txt
```

We make sure that we won’t add it to the source code version control adding it to .gitignore:


```
echo ".env" >> .gitignore
```

Add the following file on .env
```
source venv/bin/activate
export  FLASK_ENV=development
export FLASK_APP=run.py
```

### Scenario 2

On the terminal type:

```
export  FLASK_ENV=development
```

```
export FLASK_APP=run.py
```

```
flask run
```

## Unit Testing
To test the endpoints ensure that the following tools are available the follow steps below
   ### Tools:
     Postman

### Commands
  The application was tested using `nose` and coverage. To run the tests on the bash terminal use

     nosetests --with-coverage --cover-package=app  && coverage report

## Heroku Hosting

https://questioner-v.herokuapp.com/api/v1/meetups/upcoming

## GH-Pages

https://bakley.github.io/Questioner/UI/landing.html

