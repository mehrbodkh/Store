from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from DB.models.base import Base


class OrderProduct(Base):
    __tablename__ = "order_products"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order")
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product")
    count = Column(Integer)
    price_per_one = Column(Float)

    def __init__(self, order_id, product_id, count, price_per_one):
        self.order_id = order_id
        self.product_id = product_id
        self.count = count
        self.price_per_one = price_per_one
