from collections import namedtuple
from itertools import count

from rsa_encryption.tools.prime_numbers_tools import get_two_numbers_prime


euler_and_module = namedtuple("euler_and_module", "euler module")


def get_function_euler_and_module():
    """
    Function return tuple with value function euler and module.
    This tuple is namedtuple and we can use it this way:
        euler = tuple.euler
        module = tuple.module
    Thanks to this, we will not be mistaken.
    """
    first_number_prime, second_number_prime = get_two_numbers_prime()
    results = euler_and_module(
        euler=(first_number_prime - 1) * (second_number_prime - 1),
        module=first_number_prime * second_number_prime
    )
    return results


def _nwd(number: int, euler: int):
    """
    The function calculates nwd.
    """
    if number % euler == 0:
        return euler
    return _nwd(euler, number % euler)


def get_public_exponent(euler: int):
    """
    Function return public exponent.
    """
    for number in range(2, euler + 1):
        if _nwd(number, euler) == 1:
                return number
    raise ValueError

def get_private_exponent(public_exponent: int, euler: int):
    """
    Function return private exponent.
    """
    for number in count():
        if number * public_exponent % euler == 1:
            return number

def rewrite_the_contents_of_the_files(rewrite_with, write_to):
    with open(rewrite_with, "r") as file:
        with open(write_to, 'w') as file2:
            file2.write(file.read())


if __name__ == "__main__":
    a = get_function_euler_and_module()
    print(a.euler, a.module)
    
