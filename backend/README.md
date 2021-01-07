# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend using [`pipenv`](https://pipenv-fork.readthedocs.io/en/latest/) to set up a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment using [`pipenv`](https://pipenv-fork.readthedocs.io/en/latest/) for your platform can be found in the [python docs](https://packaging.python.org/tutorials/managing-dependencies/?highlight=pipenv)

#### Pipenv Install & shell

Once you have your pipenv set up and running, follow along these steps to stand up the environment:
From the root of this repo, i.e. [here](../.), run the command:

```bash
pipenv sync --dev && pipenv shell
```

This will use the [Pipfile](../Pipfile) and [Pipfile.lock](../Pipfile.lock) to install all the dependencies and subdependencies.

If you need to install additional packages, use `pipenv install [package]` and if you need to introduce more dev packages, you add the flag `--dev`, i.e. `pipenv install --dev [package]`

> Note: there is no `requirements.txt` file, as this is an old and buggy way of specifying dependencies.  To see why,  [read up on it here.](https://realpython.com/pipenv-guide/#dependency-management-with-requirementstxt)

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql $DATABASE_URL < backend/trivia.psql
```

> Note: if you've changed the database credentials from the default in this repo,
> you will need to find and replace the user (`flaskr`) with whatever your new user
> is in the [`backend/trivia.psql`](backend/trivia.psql) file.

## Running the server

From within the [root](../.) folder, first ensure your environment is active (`pipenv shell`).

To run the server, execute:

```bash
export FLASK_APP=backend/flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## API Reference

### Endpoints
All endpoints return a JSON object with at least "status_code" and "message" as keys:
- status_code: The HTTP response code, for example `200`
- message: a message with information about the response
- success: a boolean indicating success

The endpoints documentation below will not mention these, though they are always present.

#### GET

- GET `/`
  - welcome message


- GET `/categories`
  - Fetches all defined categories
  - Request Arguments: None
  - Returns: An object with a key, "categories", which is an array of objects with two keys: "id" and "type"
    - id: the id of the category in the database
    - type: the category type, a text name
    > {'categories': [{'id': 1, 'type': 'Science'}, {'id': 2, 'type': 'Art'}, {'id': 3, 'type': 'Geography'}, {'id': 4, 'type': 'History'}, {'id': 5, 'type': 'Entertainment'}, {'id': 6, 'type': 'Sports'}], }


- GET `/questions`
  - Fetches all questions in the database (paged)
  - Request Arguments: None
  - Returns: Object including the following keys:
    - categories (see above for details)
    - total_questions: the number of questions in the database
    - questions: an array of question objects
    - current_category: 'All', all questions


- GET `/categories/<int:id>/questions`
  - Fetches all questions belonging to a specific category (paged)
  - Request Argments: None
  - Returns: Object including the following keys:
    - questions: an array of questions from the category
    - total_questions: number (int) of matching questions
    - current_category: the requested category type (text)

#### POST
- POST `/questions`
  - Writes the question to the database
  - Request Arguments:
    The payload should be a JSON with keys:
    - `question`: The question in text
    - `answer`: The answer in text
    - `difficulty`: The difficulty on a scale of 1 to 5 where 1 is easy and 5 is hard
    - `category`: The id (int) of the category to which this question should belong
  - Returns: Object with key "data" which shows the posted question as it is in the database.


- POST `questions/search`
  - Searches the questions for the searchTerm and returns any matching questions
  - Request Arguments:
    There should be a search term included in your POST, i.e. `/questions?searchTerm=thing`
    - `searchTerm`: the term that should be searched
  - Returns:
    - `questions`: an array of questions matching the search term
    - `total_questions`: an integer reflecting the number of question matches to the search term
    - `current_category`: the category (text) within which the search happens

- POST `quizzes/<int:id>`
  - Fetches a random question from the category associated with id (int)
  - Request Arguments:
    - `previous_questions`: an array of ids of questions already asked
  - Returns:
    - `question`: the question object fetched

#### DELETE
- DELETE `/questions/<int:id>`
  - Deletes the specific question with that id from the database



```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
