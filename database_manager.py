from database_configs import get_db
from models import *

if __name__ == "__main__":
    db, engine = get_db(
        user='alireza',
        password='ali.1378$$',
        db='test_db',
        host='localhost',
        port=5432,
    )
    Base.metadata.drop_all(
        bind=engine,
    )
    Base.metadata.create_all(bind=engine)
