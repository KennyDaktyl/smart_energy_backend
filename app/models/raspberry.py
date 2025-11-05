from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from app.core.db import Base


class Raspberry(Base):
    __tablename__ = "raspberries"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    identifier = Column(String, unique=True)
    ip_address = Column(String)
    is_online = Column(Boolean, default=False)
    last_seen = Column(DateTime, default=datetime.utcnow)
