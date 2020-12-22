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

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle GET requests for all available categories.
4. Create an endpoint to DELETE question using a question ID.
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
6. Create a POST endpoint to get questions based on category.
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422 and 500.

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code.

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
