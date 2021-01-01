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

### Backend

The [`./backend`](./backend) directory contains a Flask and SQLAlchemy server. It defines your endpoints and can reference models.py for DB and SQLAlchemy setup.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The [`./frontend`](./frontend) directory contains a complete React frontend to consume the data from the Flask server.
It utilises the backend endpoints/API.

[View the README.md within ./frontend for more details.](./frontend/README.md)
