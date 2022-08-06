from sqlalchemy import Column, Float, String, Date, Integer, Boolean

from .database import Base


class Bill(Base):
    __tablename__ = "Bills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    amount = Column(Float)
    exp_date = Column(Date)
    code = Column(String)
    is_paid = Column(Boolean)
