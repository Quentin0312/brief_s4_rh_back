from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, Column, String


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    phone = Column(String)
    email_pro = Column(String)
    email_perso = Column(String)
