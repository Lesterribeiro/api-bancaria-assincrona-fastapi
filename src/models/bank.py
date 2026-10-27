from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AccountModel(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    holder_name = Column(String)
    balance = Column(Float, default=0.0)
    transactions = relationship("TransactionModel", back_populates="account")

class TransactionModel(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    type = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    account = relationship("AccountModel", back_populates="transactions")
