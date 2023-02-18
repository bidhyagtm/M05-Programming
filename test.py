import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
            """
            Test that it can sum a list of fractions
            """
            data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
            result = sum(data)
            self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

'''
Test Result:
    This test result shows the results of all the tests. 
    The test to add up a list of integers passed, which means the function we wrote is good.
    Another test to add up the list of fractions failed, so the function we wrote is
    not logically correct, we need to change it.
'''