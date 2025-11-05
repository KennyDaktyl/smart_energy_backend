import requests
from datetime import datetime, timedelta
from app.core.config import settings


class HuaweiAdapter:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.token = None
        self.token_expiry = datetime.utcnow()

    def _login(self):
        url = f"{settings.HUAWEI_API_URL}/login"
        resp = requests.post(
            url, json={"userName": self.username, "systemCode": self.password}
        ).json()

        if not resp.get("success"):
            raise Exception("Huawei login failed")
        self.token = resp["data"]["accessToken"]
        self.token_expiry = datetime.utcnow() + timedelta(minutes=25)

    def _ensure_token(self):
        if not self.token or datetime.utcnow() >= self.token_expiry:
            self._login()

    def get_devices(self):
        self._ensure_token()
        url = f"{settings.HUAWEI_API_URL}/getDevList"
        resp = requests.get(url, headers={"Authorization": self.token}).json()
        return resp.get("data", [])

    def get_production(self, station_code: str):
        self._ensure_token()
        url = f"{settings.HUAWEI_API_URL}/getStationRealKpi"
        resp = requests.get(
            url, headers={"Authorization": self.token}, params={"stationCodes": station_code}
        ).json()
        return resp.get("data", [])
