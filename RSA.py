from random import randint
from math import floor, sqrt
from itertools import count, chain
from tqdm import tqdm

class RSA:
    
    def _get_number_divider(self, number:int):
        """
        Metoda zwraca ilość dzielników
        """
        dzielniki = []
        for j in range(1, (floor(sqrt(number)) + 1)):
            if number % j == 0:
                dzielniki.append(j)
                dzielniki.append(int(number / j))
        return len(dzielniki)

    def _check_is_prime(self, number:int):
        if self._get_number_divider(number) == 2:
            return True
        return False

    def _get_two_number_prime(self):
        first_number, second_number = None, None
        while (first_number is None or second_number is None):
            p = randint(10, 150)
            q = randint(10, 150)
            if self._check_is_prime(p) and first_number is None:
                first_number = p
            if self._check_is_prime(q) and second_number is None:
                second_number = q
        return first_number, second_number

    def get_private(self, e: int, euler: int):
        for number in count():
            if number * e % euler == 1:
                return number

    def _check_number_is_relatively_first(self, eulera):
        for number in range(2, eulera + 1):
            if self._nwd(number, eulera) == 1:
                return number
        raise ValueError

    def _nwd(self, a, b):
        if a % b == 0:
            return b
        return self._nwd(b, a % b)


    def szyfrowanie_RSA(self):
        first_number, second_number = self._get_two_number_prime()
        euler = (first_number - 1) * (second_number - 1)
        module = first_number * second_number
        e = self._check_number_is_relatively_first(euler)
        d = self.get_private(e, euler)
        with open("public_key.txt", "w") as fp:
            fp.write(str((e, module)))
        t = []  
        with open("szyfrowany.txt", "r") as fp:
            t = [ord(element) for element in fp.read()]
        with open("szyfrowany.txt", "w") as fp:
            for number in t:
                #print(number, module, "asa")
                fp.write(str((int(number)**e)% module) + " ")
        ta = []
        with open("szyfrowany.txt", "r") as fp:
            string = fp.read()
            for element in tqdm(string.split()):
                ta.append(chr((int(element)**d)% module))
        with open("odszyfrowana.txt", "w") as fp:
            for element in ta:
                fp.write(element)

        
if __name__ == "__main__":
    a = RSA()
    a.szyfrowanie_RSA()    
                
