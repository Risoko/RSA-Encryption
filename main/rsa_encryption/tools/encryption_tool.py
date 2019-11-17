import os
from time import sleep
from tqdm import tqdm
from rsa_encryption.data_base.operation_on_table import get_public_key
from rsa_encryption.tools.others_tools import rewrite_the_contents_of_the_files

def encryption(name_public_key):
    path = input("Enter the path to the file you want to encrypt: ")
    public_key = tuple(int(element) for element in get_public_key(name_public_key).split(","))
    with open(path, 'r') as file:
        with open("helpty.txt", "w") as file2:
            file2.write(name_public_key + ".txt" + '\n')
            for element in tqdm(file.read()):
                file2.write(str(ord(element)**public_key[0] % public_key[1]) + " ")
    rewrite_the_contents_of_the_files("helpty.txt", path)
    os.remove("helpty.txt")



    
        
