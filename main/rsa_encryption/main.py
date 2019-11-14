import getopt, sys


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:", ["create_key=", ])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for option, args in opts:
        if option == "-c":
            print(args)


main()
