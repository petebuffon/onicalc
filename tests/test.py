import unittest
from onicalc import foodcalc

class TestFoodcalc(unittest.TestCase):
    def test_tofu(self):
        """
        Test foodcalc returns the proper dict.
        """
        test_dict = {'Tofu': 1.11, 'Nosh Sprout': 11.67, 'Ethanol': 233.33,
                     'Dirt': 58.33, 'Water': 55.56}
        result = foodcalc(4, "Tofu")
        self.assertEqual(result, test_dict)
    
    def test_gristle_berry(self):
        """
        Test foodcalc returns the proper dict.
        """
        test_dict = {'Gristle Berry': 2.0, 'Bristle Blossom': 12.0,
                     'Water': 240.0}
        result = foodcalc(4, "Gristle Berry")
        self.assertEqual(result, test_dict)


if __name__ == '__main__':
    unittest.main()
