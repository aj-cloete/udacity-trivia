import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL", "postgresql://flaskr:trivia-app@localhost:5432/trivia"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
