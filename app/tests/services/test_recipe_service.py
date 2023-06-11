import unittest
from app import app, db
from app.models.recipe import Recipe
from app.services.recipe_service import RecipeService

class RecipeServiceTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.recipe_service = RecipeService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_recipe(self):
        recipe_data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Flour, sugar, cocoa powder, eggs',
            'directions': 'Mix all ingredients, bake at 180°C for 30 minutes'
        }
        recipe = self.recipe_service.create(recipe_data)
        self.assertIsInstance(recipe, Recipe)
        self.assertEqual(recipe.name, 'Chocolate Cake')

    def test_update_recipe(self):
        recipe = Recipe(name='Chocolate Cake', ingredients='Flour, sugar, cocoa powder, eggs', directions='Mix all ingredients, bake at 180°C for 30 minutes')
        db.session.add(recipe)
        db.session.commit()

        recipe_data = {
            'name': 'Chocolate Brownie',
            'ingredients': 'Flour, sugar, cocoa powder, eggs, butter',
            'directions': 'Mix all ingredients, bake at 180°C for 25 minutes'
        }
        updated_recipe = self.recipe_service.update(recipe.id, recipe_data)
        self.assertIsInstance(updated_recipe, Recipe)
        self.assertEqual(updated_recipe.name, 'Chocolate Brownie')

    def test_delete_recipe(self):
        recipe = Recipe(name='Chocolate Cake', ingredients='Flour, sugar, cocoa powder, eggs', directions='Mix all ingredients, bake at 180°C for 30 minutes')
        db.session.add(recipe)
        db.session.commit()

        deleted_recipe = self.recipe_service.delete(recipe.id)
        self.assertIsInstance(deleted_recipe, Recipe)
        self.assertEqual(deleted_recipe.name, 'Chocolate Cake')

if __name__ == '__main__':
    unittest.main()
