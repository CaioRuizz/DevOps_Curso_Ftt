from app import app

import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""
    
    def test_index(self):
        """Test index"""
        expected_return = "App Funcionando"
        self.assertEqual(expected_return, app.index())
