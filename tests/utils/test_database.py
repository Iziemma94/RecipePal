import unittest
from app import app, db

class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_database_connection(self):
        with app.app_context():
            self.assertIsNotNone(db.session)

if __name__ == '__main__':
    unittest.main()
