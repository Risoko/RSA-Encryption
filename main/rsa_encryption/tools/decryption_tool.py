import os
from tqdm import tqdm
from rsa_encryption.data_base.operation_on_table import get_private_key
from rsa_encryption.tools.others_tools import rewrite_the_contents_of_the_files

def decryption(path_for_encryption_file):
    with open(path_for_encryption_file, "r") as file:
        private_key = tuple(int(element) for element in get_private_key(file.readline()).split(","))
        with open("helpty.txt", "w") as file2:
            for element in tqdm(file.read().split()):
                file2.write(chr(int(element)**private_key[0] % private_key[1]))
    rewrite_the_contents_of_the_files("helpty.txt", path_for_encryption_file)
    os.remove("helpty.txt")
               