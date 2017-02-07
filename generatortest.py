import unittest
from PrimeGenerator import Prime

class PrimeGeneratorTestCase(unittest.TestCase):
    """Tests for `PrimeGenerator.py`."""

    def test_is_three_prime(self):
        """Is three a prime?"""
        self.assertTrue(Prime(3))

    def test_negative_number(self):
        """Is a negative number dismissed from being assertTrue prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(Prime(index), msg='{} dismissed from being a prime'.format(index))

    def test_is_five_prime(self):
        """Is five a prime?"""
        self.assertTrue(Prime(5))

    def test_is_seven_prime(self):
        """Is seven a prime?"""
        self.assertTrue(Prime(7))

    def test_is_twelve_prime(self):
        """Is twelve a prime?"""
        self.assertFalse(Prime(12))

    def test_is_fortyeight_prime(self):
        """Is fortyeight a prime?"""
        self.assertFalse(Prime(48))

    def test_is_sixtyfour_prime(self):
        """Is sixtyfour a prime?"""
        self.assertFalse(Prime(64))

    def test_is_seventyone_prime(self):
        """Is seventyone a prime?"""
        self.assertTrue(Prime(71))

    def test_is_eightythree_prime(self):
        """Is eightythree a prime?"""
        self.assertTrue(Prime(83))

    def test_is_ninetyone_prime(self):
        """Is ninetyone a prime?"""
        self.assertTrue(Prime(91))

    def test_is_ninetyeight_prime(self):
        """Is ninetyeight a prime?"""
        self.assertFalse(Prime(98))


if __name__ == '__main__':
    unittest.main()