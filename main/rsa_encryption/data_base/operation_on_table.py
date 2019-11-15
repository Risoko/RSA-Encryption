from datetime import datetime

from sqlalchemy.orm import sessionmaker

from rsa_encryption.data_base.connect_database import engine
from rsa_encryption.data_base.create_column import Keys

Session = sessionmaker(bind=engine)
session = Session()

def insert_value(table_name, session=session, **kwargs):
    """Insert value on table."""
    session.add(table_name(**kwargs))
    session.commit()

def delete_unactive_key(session=session):
    all_keys = session.query(Keys).all()
    for instane in all_keys:
        if instane.keys_expire_date < datetime.now():
            session.delete(instane)
    session.commit()

            