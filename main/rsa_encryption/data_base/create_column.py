from sqlalchemy import Column, Integer, String, DateTime

from rsa_encryption.data_base.connect_database import Base, engine


class Keys(Base):
    __tablename__ = "Keys"
    private_key = Column(String, nullable=False, unique=True)
    public_key = Column(String, nullable=False, unique=True)
    name_public_key = Column(String, nullable=False, unique=True, primary_key=True)
    keys_expire_date = Column(DateTime, nullable=False)

Base.metadata.create_all(engine)