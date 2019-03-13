from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from DB.models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    fullname = Column(String)
    phone = Column(String)
    user_addresses = relationship("UserAddress")

    def __init__(self, chat_id, fullname, phone):
        self.chat_id = chat_id
        self.fullname = fullname
        self.phone = phone
