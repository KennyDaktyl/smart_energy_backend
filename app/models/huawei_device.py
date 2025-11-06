from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String

from app.core.db import Base


class HuaweiDevice(Base):
    __tablename__ = "huawei_devices"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    serial_number = Column(String, nullable=False)
    name = Column(String)
    model = Column(String)
    capacity_kw = Column(Numeric)
    last_updated = Column(DateTime, default=datetime.utcnow)
