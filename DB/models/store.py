from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

from DB.models.base import Base


class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_chat_id = Column(Integer)
    bank_card_number = Column(String(16))
    photo = Column(String)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address")
    products = relationship("Product")
    description = Column(Text)

    def __init__(self, name, owner_chat_id, bank_card_number, photo, description):
        self.name = name
        self.owner_chat_id = owner_chat_id
        self.bank_card_number = bank_card_number
        self.photo = photo
        self.description = description
