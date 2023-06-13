import unittest
from flask import Flask
from utils.database import db

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an in-memory SQLite database for testing
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_config(self):
        self.assertTrue(self.app.testing)
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], 'sqlite:///test.db')
        self.assertFalse(self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])

    def test_database_setup(self):
        with self.app.app_context():
            self.assertIsNotNone(db.engine)
            self.assertIsNotNone(db.session)

if __name__ == '__main__':
    unittest.main()
