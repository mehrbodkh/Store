from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship, backref

from DB.models.base import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    inventory = Column(Integer)
    photo = Column(String)
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store")
    description = Column(Text)

    def __init__(self, store_id, name, category, price, inventory, photo, description):
        self.store_id = store_id
        self.name = name
        self.category = category
        self.price = price
        self.photo = photo
        self.description = description
        self.inventory = inventory
