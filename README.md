# Questioner-ADC
Crowd-source questions for a meetup. Set of API endpoints

[![Maintainability](https://api.codeclimate.com/v1/badges/327b489ebb4d383d38c6/maintainability)](https://codeclimate.com/github/Bakley/Questioner-ADC/maintainability)
[![BCH compliance](https://bettercodehub.com/edge/badge/Bakley/Questioner-ADC?branch=develop)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0c82cd66a38040928a1cdcf0e8044a75)](https://www.codacy.com/app/Bakley/Questioner-ADC?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Bakley/Questioner-ADC&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/Bakley/Questioner-ADC/badge.svg?branch=develop)](https://coveralls.io/github/Bakley/Questioner-ADC?branch=develop)
[![Build Status](https://travis-ci.org/Bakley/Questioner-ADC.svg?branch=develop)](https://travis-ci.org/Bakley/Questioner-ADC)

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

