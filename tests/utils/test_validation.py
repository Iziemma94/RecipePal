import unittest
from app.utils.validation import validate_recipe_data

class ValidationTest(unittest.TestCase):

    def test_validate_recipe_data(self):
        valid_data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Flour, sugar, cocoa powder, eggs',
            'directions': 'Mix all ingredients, bake at 180°C for 30 minutes'
        }
        self.assertTrue(validate_recipe_data(valid_data))

        invalid_data = {
            'name': '',
            'ingredients': 'Flour, sugar, cocoa powder, eggs',
            'directions': 'Mix all ingredients, bake at 180°C for 30 minutes'
        }
        self.assertFalse(validate_recipe_data(invalid_data))

if __name__ == '__main__':
    unittest.main()
