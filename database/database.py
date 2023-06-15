from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: Fix this case (file executed from different "space")
try:
    from utils import getConfig
except:
    from .utils import getConfig

""" Create engine and session communicate with database """
mode = "prod"  # dev / prod

if mode == "prod":
    connection_url = (
        "postgresql://"
        + getConfig("user")
        + ":"
        + getConfig("password")
        + "@localhost/"
        + getConfig("database")
        + ""
    )
# TODO: setup secrets
else:
    connection_url = (
        "postgresql://ftsw4800_ftsw4800:azerty97480@localhost/ftsw4800_s4rh"
    )

engine = create_engine(
    connection_url,
    echo=True,
)
session = sessionmaker(bind=engine)
session = session()
