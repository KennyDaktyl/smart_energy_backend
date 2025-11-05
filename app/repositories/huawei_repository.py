from app.models.huawei_device import HuaweiDevice
from app.repositories.base_repository import BaseRepository


class HuaweiRepository(BaseRepository[HuaweiDevice]):
    def __init__(self):
        super().__init__(HuaweiDevice)
