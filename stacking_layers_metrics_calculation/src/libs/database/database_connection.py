import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.cfg_reader import CfgReader
from utils.base_exception_handler import BaseExceptionHandler



class DatabaseConnection():

    # create an engine
    engine = create_engine(f"mysql+pymysql://{CfgReader.DATABASE_USER}:{CfgReader.DATABASE_PASSWORD}@"
                           f"{CfgReader.DATABASE_HOST_URL}/{CfgReader.DATABASE_NAME}")

    # create a configured "Session" class
    session_maker = sessionmaker(bind=engine, expire_on_commit=False)

    base = declarative_base()



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
            raise BaseExceptionHandler(description=str(ex))
