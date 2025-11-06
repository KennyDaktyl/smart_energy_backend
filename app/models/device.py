from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String

from app.core.db import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    raspberry_id = Column(Integer, ForeignKey("raspberries.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    gpio_pin = Column(Integer)
    rated_power_w = Column(Numeric)
    threshold_w = Column(Numeric, default=1500)
    hysteresis_w = Column(Numeric, default=100)
    mode = Column(String, default="AUTO")
    is_on = Column(Boolean, default=False)
    last_update = Column(DateTime, default=datetime.utcnow)
