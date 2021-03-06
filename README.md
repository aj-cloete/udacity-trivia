# Full Stack API - Udacity Trivia

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students.
A bunch of team members got the idea to hold trivia on a regular basis and created a webpage
to manage the trivia app and play the game, but their API experience is limited.

That's where this repo comes in! We help them finish the trivia app, so they can start holding trivia
and seeing who's the most knowledgeable of the bunch. The application will:

1) Display questions - both all questions and per category.
   Questions will show the question, category and difficulty rating by default and can show/hide the answer.
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category.


## About the repo

This repo contains both the backend and the frontend for the app.
For **installation instructions** and **further documentation**, see the relevant links below.

> Please note: the whole repo is managed by `pipenv`.
> The easiest way to set up the environment is by running `pipenv install --dev` followed by `pipenv shell` to ensure the environment is activated.

More thorough instructions in the [backend README](./backend/README.md)

### Backend

The [`./backend`](./backend) directory contains a Flask and SQLAlchemy server.
It defines your endpoints and can reference [models.py](./backend/models.py) for DB and SQLAlchemy setup.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The [`./frontend`](./frontend) directory contains a complete React frontend to consume the data from the Flask server.
It utilises the [backend](./backend) endpoints/API.

[View the README.md within ./frontend for more details.](./frontend/README.md)

## Installation
You will need [**pipenv**](https://pipenv-fork.readthedocs.io/en/latest/) to bring up the environment.
It is recommended by the python community to set up an environment.

1. Clone the repo: `git clone https://github.com/aj-cloete/udacity-trivia.git`
2. Enter the directory: `cd udacity-trivia`
3. Set up the environment: `pipenv install --dev`
4. Specify the environment variables:

   Either create an `.env` file (`touch .env`) with the following content: (pipenv automatically loads the `.env` file when you activate the environment with `pipenv shell`)
   ```
   FLASK_APP=backend/flaskr
   FLASK_ENV=development
   DATABASE_URL="postgresql://flaskr:trivia-app@localhost:5432/trivia"
   ```
   Or export those variables above within the environment.
5. Activate the environment: `pipenv shell`

> Each process you will be launching needs to be run from within an active environment.
> This is most easily achieved by navigating to the [**udacity-trivia**](.) directory and running `pipenv shell`

## Running

There is a [Makefile](./Makefile) present which you can use to interact with the frontend and backend.
Some notable commands:
- `make frontend`: makes the frontend
- `make backend`: makes the backend
- `make db`: makes the database (assuming you're using docker)
- `make down`: brings down everything
- `make test_db`: brings up the test database (assuming you're using docker)
> These commands must be run from [the udacity-trivia directory](.), not in [backend](./backend) nor in [frontend](./frontend) directory.

If you are not able to use the `make` commands (requires docker for the databases), please ensure you're in the [udacity-trivia](.) folder.  Then use the following commands:
- **backend**:
  ```
  export FLASK_APP=backend/flaskr
  export FLASK_ENV=development
  flask run
  ```
- **frontend**: `npm start --prefix frontend`
- **database**: provided you're using docker:
  - app database: `docker-compose down && docker-compose up postgres`
  - test database: `docker-compose down && docker-compose up test_pg`

If you're not using docker, ensure that you have configured the databases correctly according to your approach of standing up the postgres database.
Details can be found in the [config.py](config.py) file for the application database
and in [backend/test_flaskr.py](./backend/test_flaskr.py) file for the test database.
> Notice the port number `54321` configured for the test database.

## Testing
To run the tests (again, from the udacity-trivia directory), make sure you have the backend database up and running (see above),
and that the environment is activated (`pipenv shell`).
Then simply run:
```
python -m unittest
```

## Troubleshooting
### The config.py file is missing
If you are seeing an error relating to the `config.py` file being missing,
you're likely trying to run the server from the `backend` folder instead of
the `udacity-trivia` folder.  Make sure your working directory is [the udacity-trivia directory](.).
Also ensure that you have set the $FLASK_APP environment variable to `backend/flaskr`

### ModuleNotFoundError: No module named 'backend'
You're likely trying to run the tests from the `backend` folder instead of
the `udacity-trivia` folder.  Make sure your working directory is [here](.).

### flask.cli.NoAppException: Could not import "flaskr"
You're likely trying to run the server from the `backend` folder instead of
the `udacity-trivia` folder.  Make sure your working directory is [here](.).

### sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused
You probably forgot to run/set up the application database.

### All unittests are failing
You probably forgot to run/set up the test database.

### Error: Cannot find module "...start.js"
You don't have node installed correctly.  Please follow the installation instructions in the [frontend README](./frontend/README.md).
