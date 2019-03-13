from sqlalchemy import Column, Integer, Text, ForeignKey, String
from sqlalchemy.orm import relationship

from DB.models.base import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_chat_id = Column(Integer)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address")
    order_products = relationship("OrderProduct")
    description = Column(Text)
    invoice_msg_uid = Column(String)

    def __init__(self, customer_chat_id, address_id, description):
        self.customer_chat_id = customer_chat_id
        self.address_id = address_id
        self.description = description
