from technical-test.app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_1(self):
        result = app._searchfunctionality("UB5 6JE", 24000)
        self.assertEqual(result, "{'UB8 2TE': ['Hillingdon', -0.478082, 51.517916], 'UB4 0TU': ['Hillingdon', -0.397889, 51.51461], 'HA4 0LN': ['Hillingdon', -0.390474, 51.555701], 'UB6 0UW': ['Ealing', -0.34005, 51.541836], 'TW13 4EX': ['Hounslow', -0.412804, 51.442892], 'TW8 8JW': ['Hounslow', -0.314343, 51.482172]}" )

    def test_2(self):
        result = app._searchfunctionality("UB5 6JE", 24000)
        self.assertEqual(result, "")
