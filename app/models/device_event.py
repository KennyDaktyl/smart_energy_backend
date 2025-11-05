from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Numeric
from datetime import datetime
from app.core.db import Base


class DeviceEvent(Base):
    __tablename__ = "device_events"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"))
    state = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    power_consumption_w = Column(Numeric)
    pv_power_w = Column(Numeric)
    total_pv_production_kwh = Column(Numeric)
    total_consumption_kwh = Column(Numeric)
