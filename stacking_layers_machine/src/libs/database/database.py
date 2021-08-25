import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.cfg_reader import CfgReader
from utils.base_exception_handler import BaseExceptionHandler



class Database():

    engine = create_engine(f"mysql+pymysql://{CfgReader.DATABASE_USER}:{CfgReader.DATABASE_PASSWORD}@"
                           f"{CfgReader.DATABASE_HOST_URL}/{CfgReader.DATABASE_NAME}")
    session_maker = sessionmaker(bind=engine, expire_on_commit=False)
    base = declarative_base()   # database connection base


    @classmethod
    def create_connection(cls):
        """
            create database connection and session_maker and base. If any problem happens in database connection set
            is_connected variable to False
        """
        try:
            # create an engine
            cls.engine = create_engine(f"mysql+pymysql://{CfgReader.DATABASE_USER}:{CfgReader.DATABASE_PASSWORD}@"
                                       f"{CfgReader.DATABASE_HOST_URL}/{CfgReader.DATABASE_NAME}")

            # create a configured "Session" class
            cls.session_maker = sessionmaker(bind=cls.engine, expire_on_commit=False)

            cls.is_connected = True
        except Exception as ex:
            cls.is_connected = False
            raise BaseExceptionHandler(error_msg=str(ex))



    @classmethod
    def create_session(cls) -> sqlalchemy.orm.session.Session:
        """
            create a new database session

            :return:
                return a new database session object
        """
        try:
            return cls.session_maker()
        except Exception as ex:
            raise BaseExceptionHandler(error_msg=str(ex))
