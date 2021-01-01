import os  # noqa
import random  # noqa
from pathlib import Path

from flask import Flask, abort, jsonify, request
from flask_cors import CORS

from backend.models import Category, Question, setup_db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):  # noqa
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile(Path(__name__).absolute().parent / "config.py")
        setup_db(app)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    cors = CORS(app, resources={r"/*": {"origins": "*"}})  # noqa

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    @app.route("/")
    def hello():
        return jsonify({"message": "hello world"})

    @app.route("/categories")
    def get_categories():
        data = Category.query.all()
        return jsonify(
            {
                "status_code": 200,
                "message": "success",
                "categories": [cat.format() for cat in data],
            }
        )

    @app.route("/questions")
    def get_questions():
        q = Question.query
        paged = q.paginate(
            per_page=QUESTIONS_PER_PAGE,
            error_out=True,
            max_per_page=QUESTIONS_PER_PAGE,
        )
        try:
            return jsonify(
                {
                    "status_code": 200,
                    "message": "success",
                    "categories": [cat.format() for cat in Category.query.all()],
                    "total_questions": q.count(),
                    "questions": [quest.format() for quest in paged.items],
                    "current_category": "All",
                }
            )
        except AttributeError:
            abort(404)

    """
    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route("/questions/<int:id>", methods=["DELETE"])
    def delete_question(id):
        try:
            question_to_delete = Question.query.get(id)
            question_to_delete.delete()
            return jsonify(
                {
                    "status_code": 200,
                    "message": f"successfully deleted question with id {id}",
                }
            )
        except AttributeError:
            abort(404)

    """
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route("/questions", methods=["POST"])
    def post_question():
        question = Question(
            question=request.json.get("question"),
            answer=request.json.get("answer"),
            difficulty=request.json.get("difficulty"),
            category=request.json.get("category"),
        )
        question.insert()
        return jsonify(
            {
                "status_code": 200,
                "message": "Successfully added question to database",
                "data": question.format(),
            }
        )

    """
    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route("/questions/search", methods=["POST"])
    def search_question():
        search_term = request.json.get("searchTerm")
        results = Question.query.filter(Question.question.ilike(f"%{search_term}%"))
        return jsonify(
            {
                "status_code": 200,
                "message": "Successfully added question to database",
                "questions": [question.format() for question in results.all()],
                "total_questions": results.count(),
                "current_category": "All",
            }
        )

    """
    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    @app.route("/categories/<int:id>/questions")
    def category_questions(id):
        q = Question.query
        if id != 0:
            q = q.filter_by(category=str(id))
        paged = q.paginate(
            per_page=QUESTIONS_PER_PAGE,
            error_out=True,
            max_per_page=QUESTIONS_PER_PAGE,
        )
        try:
            category = Category.query.get(id)
            return jsonify(
                {
                    "status_code": 200,
                    "message": "Successfully added question to database",
                    "questions": [quest.format() for quest in paged.items],
                    "total_questions": q.count(),
                    "current_category": category.format()["type"]
                    if category
                    else "All",
                }
            )
        except AttributeError:
            abort(404)

    """
    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.route("/quizzes/<int:id>", methods=["POST"])
    def quiz_questions(id):
        r_json = request.json
        previous_questions = r_json.get("previous_questions")
        cat_questions = category_questions(id).json.get("questions")
        eligible_qs = [q for q in cat_questions if q["id"] not in previous_questions]
        question = None
        if eligible_qs:
            question = random.sample(eligible_qs, k=1)[0]
        return jsonify({"status_code": 200, "message": "success", "question": question})

    """
    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 404,
                    "message": "The record you requested was not found",
                }
            ),
            404,
        )

    @app.errorhandler(422)
    def not_processable(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 422,
                    "message": "Your request is not processable",
                }
            ),
            422,
        )

    return app
