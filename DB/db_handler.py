import logging

from sqlalchemy import distinct

from DB.models.address import Address
from DB.models.base import Session, Base, engine
from DB.models.product import Product
from DB.models.store import Store
from DB.models.user import User
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


@db_persist
def add_store(name, owner_chat_id, bank_card_number, photo=None, description=None):
    store = Store(name=name, owner_chat_id=owner_chat_id, bank_card_number=bank_card_number, photo=photo,
                  description=description)
    session.add(store)


def get_store(store_id):
    return session.query(Store).filter(Store.id == store_id).one_or_none()


@db_persist
def set_store_address(store_id, lat, lng):
    address = Address(city=None, address=None, latitude=lat, longitude=lng)
    session.add(address)
    store = get_store(store_id)
    store.address = address


@db_persist
def add_store_product(store_id, name, category, price, inventory, photo, description):
    product = Product(store_id, name, category, price, inventory, photo, description)
    session.add(product)


def get_product_by_id(product_id):
    return session.query(Product).filter(Product.id == product_id).one_or_none()


def get_product_by_category(category):
    return session.query(Product).filter(Product.category == category).all()


def get_product_by_store_id(store_id):
    return session.query(Product).filter(Product.store_id == store_id).all()


@db_persist
def set_product_inventory(product_id, inventory):
    product = get_product_by_id(product_id)
    product.inventory = inventory


def get_product_categories():
    categories = session.query(distinct(Product.category)).all()
    categories = [category[0] for category in categories]
    result = []
    for category in categories:
        product_count = session.query(Product).filter(Product.category == category).count()
        result.append((category, product_count))
    return result
