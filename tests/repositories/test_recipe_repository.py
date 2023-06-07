import unittest
from app import app, db
from app.models.recipe import Recipe
from app.repositories.recipe_repository import RecipeRepository

class RecipeRepositoryTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.recipe_repository = RecipeRepository()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_recipe(self):
        recipe_data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Flour, sugar, cocoa powder, eggs, butter',
            'directions': '1. Mix ingredients, 2. Bake in oven',
            'category': 'Dessert'
        }
        recipe = self.recipe_repository.create(recipe_data)
        self.assertIsInstance(recipe, Recipe)
        self.assertEqual(recipe.name, 'Chocolate Cake')

    def test_update_recipe(self):
        recipe = Recipe(name='Chocolate Cake', ingredients='Flour, sugar, cocoa powder, eggs, butter', directions='1. Mix ingredients, 2. Bake in oven', category='Dessert')
        db.session.add(recipe)
        db.session.commit()

        recipe_data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Flour, sugar, cocoa powder, eggs, butter, oil',
            'directions': '1. Mix ingredients, 2. Bake in oven',
            'category': 'Dessert'
        }
        updated_recipe = self.recipe_repository.update(recipe.id, recipe_data)
        self.assertIsInstance(updated_recipe, Recipe)
        self.assertEqual(updated_recipe.ingredients, 'Flour, sugar, cocoa powder, eggs, butter, oil')

    def test_delete_recipe(self):
        recipe = Recipe(name='Chocolate Cake', ingredients='Flour, sugar, cocoa powder, eggs, butter', directions='1. Mix ingredients, 2. Bake in oven', category='Dessert')
        db.session.add(recipe)
        db.session.commit()

        deleted_recipe = self.recipe_repository.delete(recipe.id)
        self.assertIsInstance(deleted_recipe, Recipe)
        self.assertEqual(deleted_recipe.name, 'Chocolate Cake')

if __name__ == '__main__':
    unittest.main()
