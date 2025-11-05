from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.device_event import DeviceEvent


class DeviceEventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DeviceEvent
        include_fk = True
        load_instance = True
