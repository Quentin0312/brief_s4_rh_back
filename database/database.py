import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    from utils import getConfig
except:
    from .utils import getConfig


connection_url = os.environ.get("CONNECTION_URL")
if connection_url is None:
    connection_url = (
        "postgresql://"
        + getConfig("user")
        + ":"
        + getConfig("password")
        + "@localhost/"
        + getConfig("database")
        + ""
    )

engine = create_engine(
    connection_url,
    echo=True,
)
session = sessionmaker(bind=engine)
session = session()
