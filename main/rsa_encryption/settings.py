from decouple import config

RANGE_OF_PRIME_NUMBERS = {
    "min": 10,
    "max": 190
}
DEFAULT_PUBLIC_KEY_NAME = "PublicKey" 

DATABASE = {
    'type': config("TYPE"),
    'user': config("USER"),
    'password': config("PASSWORD"),
    'localhost': config("LOCALHOST"),
    'database_name': config("DATABASE_NAME")
}                