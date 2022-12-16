from typing import Tuple

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()


def get_db(
        user: str, password: str, db: str, host: str, port: int
) -> Tuple[Session, Engine]:
    info = {"user": user, "pw": password, "db": db, "host": host, "port": port}
    sqlalchemy_database_url = (
            "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % info
    )
    engine = create_engine(sqlalchemy_database_url)
    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = local_session()
    automap_base()
    return db, engine
