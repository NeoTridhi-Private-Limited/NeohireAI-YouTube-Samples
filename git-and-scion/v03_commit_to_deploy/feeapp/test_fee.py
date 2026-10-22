import unittest
from fee import delivery_fee


class FeeTest(unittest.TestCase):
    def test_free_above_499(self):
        self.assertEqual(delivery_fee(9, 520), 0)

    def test_near(self):
        self.assertEqual(delivery_fee(2, 200), 25)

    def test_far(self):
        self.assertEqual(delivery_fee(6, 200), 49)

    def test_cap(self):
        self.assertEqual(delivery_fee(25, 200), 99)


if __name__ == "__main__":
    unittest.main()
