from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from datetime import datetime
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
