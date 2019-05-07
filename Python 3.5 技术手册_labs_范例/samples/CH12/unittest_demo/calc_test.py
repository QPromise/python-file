import unittest
import calc

class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_plus(self):
        expected = 5;
        result = calc.plus(*self.args);
        self.assertEqual(expected, result)

    def test_minus(self):
        expected = 1;
        result = calc.minus(*self.args);
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()