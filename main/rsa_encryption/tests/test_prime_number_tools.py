from unittest import TestCase, main

from rsa_encryption.tools.prime_numbers_tools import (
    _get_number_divisiors, _check_is_prime_number, get_two_numbers_prime
)

class TestGetNumberDivisiors(TestCase):
    
    def test_with_prime_numbers(self):
        self.assertTrue(_get_number_divisiors(5) == 1)
        self.assertTrue(_get_number_divisiors(97) == 1)
        self.assertTrue(_get_number_divisiors(89) == 1)

    def test_with_numbers_that_are_not_prime(self):
        self.assertTrue(_get_number_divisiors(6) != 1)
        self.assertTrue(_get_number_divisiors(15) != 1)
        
    def test_with_be_smaller_than_or_equal_to_one(self):
       with self.assertRaises(ValueError, msg="Number must be greater than 1."):
           _get_number_divisiors(1)
       with self.assertRaises(ValueError, msg="Number must be greater than 1."):
           _get_number_divisiors(-1)

class TestCheckIsPrimeNumber(TestCase):

    def test_with_prime_numbers(self):
        self.assertTrue(_check_is_prime_number(5))
        self.assertTrue(_check_is_prime_number(97))
        self.assertTrue(_check_is_prime_number(89))

    def test_with_numbers_that_are_not_prime(self):
        self.assertFalse(_check_is_prime_number(6))
        self.assertFalse(_check_is_prime_number(15))
        self.assertFalse(_check_is_prime_number(20))

class TestGetTwoNumbersPrime(TestCase):
    
    def test_function_return_two_prime_number(self):
        first, second = get_two_numbers_prime()
        self.assertTrue(_check_is_prime_number(first))
        self.assertTrue(_check_is_prime_number(second))
           
if __name__ == '__main__':
    main()