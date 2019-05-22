import logging

from sqlalchemy.exc import SQLAlchemyError
from db.models.base import Session

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
session = Session()


def db_persist(func):
    def persist(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            session.commit()
            logger.info("SUCCESS: " + func.__name__)
            return res
        except SQLAlchemyError as e:
            logger.error("FAILURE: " + func.__name__)
            logger.error(e)
            session.rollback()
            return False

    return persist
