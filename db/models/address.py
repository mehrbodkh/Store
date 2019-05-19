from sqlalchemy import Column, Integer, String

from db.models.base import Base


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    address = Column(String)
    latitude = Column(String)
    longitude = Column(String)

    def __init__(self, city, address, latitude, longitude):
        self.city = city
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
