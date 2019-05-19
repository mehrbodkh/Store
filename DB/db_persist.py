from sqlalchemy.exc import SQLAlchemyError

from db.db_handler import session, logger


def db_persist(func):
    def persist(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            session.commit()
            logger.info("success calling db func: " + func.__name__)
            return res
        except SQLAlchemyError as e:
            logger.error(e.args)
            session.rollback()
            return False

    return persist
