"""
prime.pyのテストスクリプト
"""
import unittest

from comp_prog_lib.math.prime import is_prime


class IsPrimeTest(unittest.TestCase):

    def test_is_prime(self):
        primes = set([2, 3, 5, 7, 11, 13])
        for i in range(1, 17):
            if i in primes:
                self.assertTrue(is_prime(i))
            else:
                self.assertFalse(is_prime(i))
