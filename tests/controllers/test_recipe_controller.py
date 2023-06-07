import json
import unittest
from app import app, db
from app.models.recipe import Recipe

class RecipeControllerTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_recipe(self):
        data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Flour, sugar, cocoa powder, eggs, butter',
            'directions': '1. Mix ingredients, 2. Bake in oven',
            'category': 'Dessert'
        }
        response = self.app.post('/api/recipes', data=json.dumps(data),
                                 headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Recipe created successfully', response.data)

    def test_update_recipe(self):
        recipe = Recipe(name='Chocolate Cake', ingredients='Flour, sugar, cocoa powder, eggs, butter', directions='1. Mix ingredients, 2. Bake in oven', category='Dessert')
        db.session.add(recipe)
        db.session.commit()

        data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Flour, sugar, cocoa powder, eggs, butter, oil',
            'directions': '1. Mix ingredients, 2. Bake in oven',
            'category': 'Dessert'
        }
        response = self.app.put('/api/recipes/1', data=json.dumps(data),
                                headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Recipe updated successfully', response.data)

    def test_delete_recipe(self):
        recipe = Recipe(name='Chocolate Cake', ingredients='Flour, sugar, cocoa powder, eggs, butter', directions='1. Mix ingredients, 2. Bake in oven', category='Dessert')
        db.session.add(recipe)
        db.session.commit()

        response = self.app.delete('/api/recipes/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Recipe deleted successfully', response.data)

if __name__ == '__main__':
    unittest.main()
