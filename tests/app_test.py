from werkzeug.wrappers import response
from app import app

import requests

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


    def test_rota_bhaskara(self):
        url = "http://localhost:3000/bhaskara"

        payload = {
            "a": 4,
            "b": -4,
            "c": 1
        }
        headers = {"Content-Type": "application/json"}

        response = requests.request("POST", url, json=payload, headers=headers).json()

        expected_result = [0.5, 0.5]

        self.assertEquals(response, expected_result)


    def test_outra_rota_import(self):
        expected_response = 'Rota Funcionando'

        response = app.outra_rota()

        self.assertEquals(response, expected_response)


    def test_outra_rota_http(self):
        expected_response = 'Rota Funcionando'

        url = 'http://localhost:3000/outraRota'

        response = requests.get(url)

        self.assertEquals(response, expected_response)

        
