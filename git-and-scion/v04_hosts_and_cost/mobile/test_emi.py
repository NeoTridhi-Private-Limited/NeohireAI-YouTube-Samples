import unittest
from emi import emi


class EmiTest(unittest.TestCase):
    def test_zero_rate(self):
        self.assertEqual(emi(120000, 0, 12), 10000.0)

    def test_home_loan(self):
        self.assertAlmostEqual(emi(100000, 12, 12), 8884.88, places=2)


if __name__ == "__main__":
    unittest.main()
