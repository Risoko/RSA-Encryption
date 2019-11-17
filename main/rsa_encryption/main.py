import getopt, os, sys
from datetime import datetime, timedelta

from rsa_encryption.settings import PATH_FOR_PUBLIC_KEY, KEYS_EXPIRE
from rsa_encryption.tools.keys_tool import create_keys
from rsa_encryption.tools.encryption_tool import encryption
from rsa_encryption.tools.decryption_tool import decryption
from rsa_encryption.data_base.create_column import Keys
from rsa_encryption.data_base.operation_on_table import delete_unactive_key, insert_value


def main():
    """
    Main program function.
    """
    delete_unactive_key()
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "c:e:d:s")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for option, arg in opts:
        if option == "-c":
            public_key, private_key = create_keys()
            while True:
                try:
                    insert_value(
                        table_name=Keys,
                        name_public_key=arg + ".txt",
                        keys_expire_date=datetime.now() + timedelta(
                            days=KEYS_EXPIRE['DAYS'],
                            minutes=KEYS_EXPIRE['MINUTES'],
                            seconds=KEYS_EXPIRE['SECONDS']
                        ),
                        private_key=private_key,
                        public_key=public_key
                    )
                except Exception as err:
                    print("Make sure that the key name you provided does not exist.")
                    print("If you are sure that the name you have entered is correct, press y")
                    print("The key probably already exists and the next pair will be drawn.")
                    output = input("Change the key name, press N, generate a new key pair, press Y.: ")
                    if output.upper() == "Y":
                        public_key, private_key = create_keys()
                        continue
                    else:
                        print("Stop program.")
                        break
                else:    
                    with open(PATH_FOR_PUBLIC_KEY + '/' + arg + '.txt', 'w') as file:
                        file.write(str(public_key))
                    break
        if option == '-e':
            encryption(arg)
        if option == '-d':
            decryption(arg)
        if option == '-s':
            for _, _, f in os.walk(PATH_FOR_PUBLIC_KEY):
                for element in f:
                    print(element[:-4])

main()
