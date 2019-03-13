from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from DB.models.base import Base


class OrderPayment(Base):
    __tablename__ = "order_payments"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)
    order = relationship("Order")
    amount = Column(String)
    msg_uid = Column(String)
    traceNo = Column(String)

    def __init__(self, order_id, amount, msg_uid, traceNo):
        self.order_id = order_id
        self.amount = amount
        self.msg_uid = msg_uid
        self.traceNo = traceNo
