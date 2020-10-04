import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from ..common.settings import get_databse_settings

settings = get_databse_settings()

SQL_ALCHEMY_DATABASE_URL = settings.postgres_url

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def test_db_connection():
    attempts = 0
    while attempts < 5:
        try:
            engine.connect()
            logging.info('Successfully connected to the database')
            break
        except OperationalError as err:
            attempts += 1
            logging.error('Error connecting to the Database: ' + str(err.orig))
            if attempts == 5:
                raise
