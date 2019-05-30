import sys
import unittest
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
import app


class FlaskTestCase(unittest.TestCase):

    def test_UB5_6JE(self):
        result = app.search_postcode_radius(24000, "UB5 6JE")
        print(" Running test_UB5_6JE")
        self.assertEqual(result, {'HA4 0LN': ['Hillingdon', -0.390474, 51.555701], 'TW13 4EX': ['Hounslow', -0.412804, 51.442892], 'TW8 8JW': ['Hounslow', -0.314343, 51.482172], 'UB4 0TU': ['Hillingdon', -0.397889, 51.51461], 'UB6 0UW': ['Ealing', -0.34005, 51.541836], 'UB8 2TE': ['Hillingdon', -0.478082, 51.517916]})

    def test_NW1_9JB(self):
        result = app.search_postcode_radius(23000, "NW1 9JB")
        print(" Running test_NW1_9JB")
        self.assertEqual(result, {'NW1 9EX': ['Camden', -0.13693, 51.543913]})

    def test_CM2_6XJ(self):
        result = app.search_postcode_radius(2000, "CM2 6XJ")
        print("  Running test_CM2_6XJ")
        self.assertEqual(result, {'CM2 6XE': ['Chelmsford', 0.495698, 51.732632]})

    def test_LU1_3EN(self):
        result = app.search_postcode_radius(18000, "LU1 3EN")
        print(" Running test_LU1_3EN")
        self.assertEqual(result,{'AL1 2RJ': ['St Albans', -0.341337, 51.741753], 'HP3 9AA': ['Dacorum', -0.474067, 51.739299], 'LU1 3JH': ['Luton', -0.3982, 51.873519], 'LU5 4XZ': ['Central Bedfordshire', -0.514047, 51.890604]})

    def test_RH19_1QL(self):
        result = app.search_postcode_radius(5000, "RH19 1QL")
        print(" Running test_RH19_1QL")
        self.assertEqual(result, {'RH15 9QT': ['Mid Sussex', -0.149078, 50.950564], 'RH19 1QL': ['Mid Sussex', -0.035134, 51.137408]})

    def test_GU9_9QT(self):
        result = app.search_postcode_radius(25000, "GU9 9QT")
        print(" Running test_GU9_9QT")
        self.assertEqual(result, {'GU14 7QL': ['Rushmoor', -0.760871, 51.28861], 'GU34 2QS': ['East Hampshire', -0.956537, 51.157421], 'GU7 1DR': ['Waverley', -0.606494, 51.187514], 'GU9 9QJ': ['Waverley', -0.783878, 51.218514]})

if __name__ == '__main__':
    unittest.main()
