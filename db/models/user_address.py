from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.models.base import Base


class UserAddress(Base):
    __tablename__ = "user_address"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address")

    def __init__(self, user, address):
        self.user = user
        self.address = address
