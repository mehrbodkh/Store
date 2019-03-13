from sqlalchemy import Column, Integer, String

from DB.models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    chat_id = Column(String)
    fullname = Column(String)
    phone = Column(String)

    def __init__(self, chat_id, fullname, phone):
        self.chat_id = chat_id
        self.fullname = fullname
        self.phone = phone
