import getopt, sys
from datetime import datetime, timedelta

from rsa_encryption.settings import DEFAULT_PUBLIC_KEY_NAME
from rsa_encryption.tools.keys_tool import create_keys

from rsa_encryption.data_base.create_column import Keys
from rsa_encryption.data_base.operation_on_table import delete_unactive_key, insert_value


def main():
    delete_unactive_key()
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "c:", ["create_key=",])
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
                        keys_expire_date=datetime.now() + timedelta(minutes=2),
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
                    with open(arg + '.txt', 'w') as file:
                        file.write(str(public_key))
                    break





main()
