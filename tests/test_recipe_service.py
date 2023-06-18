import unittest
from unittest.mock import patch
from app.models import Recipe
from app.services.recipe_service import RecipeService

class RecipeServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any necessary configurations or dependencies
        pass

    @patch('app.repositories.recipe_repository.RecipeRepository.get_all_recipes')
    def test_get_all_recipes(self, mock_get_all_recipes):
        # Mock the RecipeRepository method
        mock_get_all_recipes.return_value = [
            Recipe(id=1, name='Recipe 1'),
            Recipe(id=2, name='Recipe 2'),
        ]

        # Call the get_all_recipes method
        recipes = RecipeService.get_all_recipes()

        # Check if the RecipeRepository method is called correctly
        mock_get_all_recipes.assert_called_once()

        # Check the return value
        self.assertEqual(len(recipes), 2)
        self.assertEqual(recipes[0].name, 'Recipe 1')
        self.assertEqual(recipes[1].name, 'Recipe 2')

    @patch('app.repositories.recipe_repository.RecipeRepository.get_recipe_by_id')
    def test_get_recipe_by_id(self, mock_get_recipe_by_id):
        # Mock the RecipeRepository method
        mock_get_recipe_by_id.return_value = Recipe(id=1, name='Recipe 1')

        # Call the get_recipe_by_id method
        recipe = RecipeService.get_recipe_by_id(1)

        # Check if the RecipeRepository method is called correctly
        mock_get_recipe_by_id.assert_called_once_with(1)

        # Check the return value
        self.assertEqual(recipe.name, 'Recipe 1')

    @patch('app.repositories.recipe_repository.RecipeRepository.create_recipe')
    def test_create_recipe(self, mock_create_recipe):
        # Call the create_recipe method
        recipe_data = {'name': 'New Recipe'}
        RecipeService.create_recipe(recipe_data)

        # Check if the RecipeRepository method is called correctly
        mock_create_recipe.assert_called_once_with(recipe_data)

    @patch('app.repositories.recipe_repository.RecipeRepository.get_recipe_by_id')
    @patch('app.repositories.recipe_repository.RecipeRepository.update_recipe')
    def test_update_recipe(self, mock_update_recipe, mock_get_recipe_by_id):
        # Mock the RecipeRepository methods
        mock_get_recipe_by_id.return_value = Recipe(id=1, name='Recipe 1')

        # Call the update_recipe method
        updated_data = {'name': 'Updated Recipe'}
        success, message = RecipeService.update_recipe(1, updated_data)

        # Check if the RecipeRepository methods are called correctly
        mock_get_recipe_by_id.assert_called_once_with(1)
        mock_update_recipe.assert_called_once_with(mock_get_recipe_by_id.return_value, updated_data)

        # Check the return values
        self.assertTrue(success)
        self.assertEqual(message, 'Recipe updated successfully')

    @patch('app.repositories.recipe_repository.RecipeRepository.get_recipe_by_id')
    @patch('app.repositories.recipe_repository.RecipeRepository.delete_recipe')
    def test_delete_recipe(self, mock_delete_recipe, mock_get_recipe_by_id):
        # Mock the RecipeRepository methods
        mock_get_recipe_by_id.return_value = Recipe(id=1, name='Recipe 1')

        # Call the delete_recipe method
        success, message = RecipeService.delete_recipe(1)

        # Check if the RecipeRepository methods are called correctly
        mock_get_recipe_by_id.assert_called_once_with(1)
        mock_delete_recipe.assert_called_once_with(mock_get_recipe_by_id.return_value)

        # Check the return values
        self.assertTrue(success)
        self.assertEqual(message, 'Recipe deleted successfully')

if __name__ == '__main__':
    unittest.main()
