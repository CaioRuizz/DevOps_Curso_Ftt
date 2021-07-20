from app import app

import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def test_return_backwards_string(self):
        """Test return backwards simple string"""
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, app.returnBackwardsString(random_string))
    
    def test_index(self):
        """Test index"""
        expected_return = "App Funcionando"
        self.assertEqual(expected_return, app.index())
