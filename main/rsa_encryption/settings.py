from decouple import config

RANGE_OF_PRIME_NUMBERS = {
    "min": 10,
    "max": 190
}

DATABASE = {
    'type': config("TYPE"),
    'user': config("USER"),
    'password': config("PASSWORD"),
    'localhost': config("LOCALHOST"),
    'database_name': config("DATABASE_NAME")
}           

PATH_FOR_PUBLIC_KEY = "/home/risoko/Pulpit/public_key"

KEYS_EXPIRE = {
    "DAYS": 0,
    "MINUTES": 10,
    "SECONDS": 0
}