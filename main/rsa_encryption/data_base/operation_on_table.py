import os
from datetime import datetime

from sqlalchemy.orm import sessionmaker

from rsa_encryption.data_base.connect_database import engine
from rsa_encryption.data_base.create_column import Keys
from rsa_encryption.settings import PATH_FOR_PUBLIC_KEY

Session = sessionmaker(bind=engine)
session = Session()


class PublicKeyDoesNotExist(Exception):
    pass


class PrivateKeyDoesNotExist(Exception):
    pass


def insert_value(table_name, session=session, **kwargs):
    """
    Insert value on table.
    """
    session.add(table_name(**kwargs))
    session.commit()


def delete_unactive_key(session=session):
    """
    Delete unactive key.
    """
    all_keys = session.query(Keys).all()
    for instane in all_keys:
        if instane.keys_expire_date < datetime.now():
            os.remove(PATH_FOR_PUBLIC_KEY + "/" + instane.name_public_key)
            session.delete(instane)
    session.commit()


def get_public_key(name: str, session=session):
    """
    Function return public key with entry name.
    If key does not exist function raise Exception.
    """
    all_keys = session.query(Keys).all()
    for instance in all_keys:
        if instance.name_public_key == name + '.txt':
            return instance.public_key[1:-1]
    raise PublicKeyDoesNotExist("The public key with the given name does not exist or has expired.")


def get_private_key(name: str, session=session):
    """
    Function return private key with entry name.
    If key does not exist function raise Exception.
    """
    all_keys = session.query(Keys).all()
    for instance in all_keys:
        if instance.name_public_key == name[:-1]:
            return instance.private_key[1:-1]
    raise PrivateKeyDoesNotExist("The private key with the given name does not exist or has expired.")