import logging

from sqlalchemy import distinct

from DB.models.address import Address
from DB.models.base import Session, Base, engine
from DB.models.order import Order
from DB.models.order_payment import Payment
from DB.models.order_product import OrderProduct
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
    return session.query(Product).filter(Product.id == product_id, Product.inventory != 0,
                                         Product.inventory.isnot(None)).one_or_none()


def get_products_by_category(category):
    return session.query(Product).filter(Product.category == category, Product.inventory != 0,
                                         Product.inventory.isnot(None)).all()


def get_products_by_store_id(store_id):
    return session.query(Product).filter(Product.store_id == store_id, Product.inventory != 0,
                                         Product.inventory.isnot(None)).all()


def find_products_by_name(name):
    return session.query(Product).filter(Product.name.like("%" + name + "%"), Product.inventory != 0,
                                         Product.inventory.isnot(None)).all()


@db_persist
def set_product_inventory(product_id, inventory):
    product = get_product_by_id(product_id)
    product.inventory = inventory


def get_product_categories():
    categories = session.query(distinct(Product.category)).filter(Product.inventory != 0,
                                                                  Product.inventory is not None).all()
    categories = [category[0] for category in categories]
    result = []
    for category in categories:
        product_count = session.query(Product).filter(Product.category == category).count()
        result.append((category, product_count))
    return result


@db_persist
def add_order(customer_chat_id, address_id, description):
    order = Order(customer_chat_id, address_id, description)
    session.add(order)


def get_order_by_id(order_id):
    return session.query(Order).filter(Order.id == order_id).one_or_none()


def get_customer_orders(chat_id):
    return session.query(Order).filter(Order.customer_chat_id == chat_id).all()


def get_order_by_msg_uid(msg_uid):
    return session.query(Order).filter(Order.invoice_msg_uid == msg_uid).one_or_none()


@db_persist
def add_order_product(order_id, product_id, count, price_per_one):
    order_product = OrderProduct(order_id, product_id, count, price_per_one)
    session.add(order_product)


@db_persist
def set_order_invoice(order_id, msg_uid):
    order = get_order_by_id(order_id)
    order.invoice_msg_uid = msg_uid


@db_persist
def set_order_address(order_id, address=None, lat=None, lng=None):
    if lat and lng:
        address = Address(city=None, address=None, latitude=lat, longitude=lng)
        session.add(address)
    order = get_order_by_id(order_id)
    order.address = address


@db_persist
def add_payment(order_id, amount, msg_uid, traceNo):
    order_payment = Payment(order_id, amount, msg_uid, traceNo)
    session.add(order_payment)


def get_payment(order_id):
    return session.query(Payment).filter(Payment.order_id == order_id).one_or_none()


def get_customer_current_order(customer_chat_id):
    return session.query(Order).filter(Order.invoice_msg_uid.is_(None),
                                       Order.customer_chat_id == customer_chat_id).one_or_none()


def get_current_order_products(order_id):
    return session.query(OrderProduct).filter(OrderProduct.order_id == order_id).all()
