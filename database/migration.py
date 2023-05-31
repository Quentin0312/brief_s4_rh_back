from database import engine

from entity.employee import Employee, Base

"""Create all tables"""
Base.metadata.create_all(engine)
