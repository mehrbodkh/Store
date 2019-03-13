import logging

from DB.models.base import Session, Base, engine
from DB.models.user import User
from DB.models.address import Address
from DB.models.user_address import UserAddress

Base.metadata.create_all(engine)
session = Session()
logger = logging.getLogger()


def db_persist(func):
    def persist(*args, **kwds):
        func(*args, **kwds)
        try:
            session.commit()
        except Exception as e:
            logger.error(e)
            session.rollback()
            return None

    return persist


@db_persist
def add_user(chat_id, fullname=None, phone=None):
    user = User(chat_id, fullname, phone)
    session.add(user)


def get_user(chat_id):
    return session.query(User).filter(User.chat_id == chat_id).one_or_none()


@db_persist
def add_user_address(chat_id, lat, lng):
    address = Address(city=None, address=None, latitude=lat, longitude=lng)
    session.add(address)
    user_address = UserAddress(get_user(chat_id), address)
    session.add(user_address)


def get_user_addresses(chat_id):
    user = get_user(chat_id)
    return [user_address.address for user_address in user.user_addresses]
