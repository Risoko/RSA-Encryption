from math import floor, sqrt
from random import randint

from rsa_encryption.settings import RANGE_OF_PRIME_NUMBERS


def _get_number_divisiors(number: int):
    """
    Function return number of divisiors of a given number.
    """
    if number <= 1:
        raise ValueError("Number must be greater than 1.")
    return len(list(divisior for divisior in range(1, floor(sqrt(number) + 1)) \
                                                   if number % divisior == 0))


def _check_is_prime_number(number: int):
    """
    Function, checks if number is prime.
    """
    return True if _get_number_divisiors(number) == 1 else False


def get_two_numbers_prime():
    """
    Function return two random number prime.
    """
    first_number_prime, second_number_prime = None, None
    min_value, max_value = RANGE_OF_PRIME_NUMBERS["min"], RANGE_OF_PRIME_NUMBERS["max"]
    while first_number_prime is None or second_number_prime is None:
        first_random_number = randint(min_value, max_value)
        second_random_number = randint(min_value, max_value)
        if _check_is_prime_number(first_random_number) and first_number_prime is None:
            first_number_prime = first_random_number
        if _check_is_prime_number(second_random_number) and second_number_prime is None:
            second_number_prime = second_random_number
    return first_number_prime, second_number_prime


if __name__ == "__main__":
    print(get_two_numbers_prime())
        