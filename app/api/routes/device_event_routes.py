import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.repositories.device_event_repository import DeviceEventRepository
from app.schemas.device_event_schema import DeviceEventCreate, DeviceEventOut

router = APIRouter(prefix="/device-events", tags=["Device Events"])

repo = DeviceEventRepository()
logger = logging.getLogger(__name__)


@router.post("/", response_model=DeviceEventOut)
def log_device_state(payload: DeviceEventCreate, db: Session = Depends(get_db)):
    timestamp = payload.timestamp or datetime.now(timezone.utc)

    event = repo.create_state_event(
        db,
        device_id=payload.device_id,
        pin_state=payload.pin_state,
        trigger_reason=payload.trigger_reason,
        power_kw=payload.power_kw,
        timestamp=timestamp,
    )

    logger.info(
        "Device event persisted",
        extra={
            "device_id": payload.device_id,
            "pin_state": payload.pin_state,
            "trigger_reason": payload.trigger_reason,
            "power_kw": payload.power_kw,
            "timestamp": timestamp.isoformat(),
        },
    )

    return event


@router.get("/device/{device_id}", response_model=list[DeviceEventOut])
def list_device_events(
    device_id: int, limit: int = Query(200, ge=1, le=1000), db: Session = Depends(get_db)
):
    return repo.list_for_device(db, device_id=device_id, limit=limit)
