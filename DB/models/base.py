from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from DB.config import DbConfig

engine = create_engine(DbConfig.database_url)
Session = sessionmaker(bind=engine)

Base = declarative_base()
