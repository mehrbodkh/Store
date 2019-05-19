from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from main_config import DatabaseConfig

engine = create_engine(DatabaseConfig.database_url)
Session = sessionmaker(bind=engine)

Base = declarative_base()
