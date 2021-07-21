from app import app

import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""
    
    def test_index(self):
        """Test index"""
        expected_return = "App Funcionando"
        self.assertEqual(expected_return, app.index())

    def test_bhaskara(self):
        a = 4
        b = -4
        c = 1
        self.assertEqual('[0.5, 0.5]', app.bhaskara(a, b, c))

    def test_multiplicacao(self):
        a = 5
        b = 6
        expected_result = 30
        self.assertEqual(expected_result, app.multiplicacao(a,b))

    def test_soma(self):
        a = 5
        b = 6
        expected_result = 11
        self.assertEqual(expected_result, app.soma(a,b))

    def test_divisao(self):
        a = 12
        b = 6
        expected_result = 2
        self.assertEqual(expected_result, app.divisao(a,b))
