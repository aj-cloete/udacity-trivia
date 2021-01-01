import unittest

from backend.flaskr import create_app
from backend.models import get_db, setup_db


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "trivia_test"
        self.database_path = "postgresql://test:test@localhost:54321/trivia_test"
        self.app = create_app({"SQLALCHEMY_DATABASE_URI": self.database_path})
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        setup_db(self.app)
        self.db = get_db()

    def tearDown(self):
        """Executed after each test"""
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    """
    TODO
    Write at least one test for each endpoint for successful operation and for expected errors.
    """


class TestHome(TriviaTestCase):
    def test_home(self):
        res = self.client().get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json.get("message"), "hello world")

    def test_get_categories(self):
        res = self.client().get("/categories")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json.get("message"), "success")

    def test_get_questions(self):
        res = self.client().get("/questions")
        self.assertEqual(res.json.get("message"), "success")
        self.assertEqual(res.status_code, 200)

    def test_delete_question(self):
        res = self.client().delete("/questions/100")
        self.assertEqual(res.status_code, 404)

    def test_post_question(self):
        q = "Is this the real world?"
        payload = {"question": q}
        res = self.client().post("/questions", json=payload)
        self.assertEqual(200, res.status_code)
        self.assertEqual(res.json.get("data").get("question"), q)

    def test_search_question(self):
        q = "Is this the real world?"
        payload = {"question": q}
        self.client().post("/questions", json=payload)

        res = self.client().post("/questions/search", json={"searchTerm": "real"})
        self.assertEqual(len(res.json.get("questions")), 1)

    def test_get_category_questions(self):
        q = "Is this a science question?"
        payload = {"question": q, "category": "1"}
        self.client().post("/questions", json=payload)

        res = self.client().get("categories/1/questions")
        self.assertEqual(len(res.json.get("questions")), 1)

    def test_post_quiz(self):
        q = "Is this a science question?"
        payload = {"question": q, "category": "1"}
        self.client().post("/questions", json=payload)

        q = "Is this not a science question?"
        payload = {"question": q, "category": "1"}
        self.client().post("/questions", json=payload)

        res = self.client().post("quizzes/0", json={"previous_questions": []})
        self.assertEqual(res.json.get("question").get("category"), "1")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
