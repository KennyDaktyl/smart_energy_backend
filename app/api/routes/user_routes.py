from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.core.dependencies import get_current_user
from app.core.security import decrypt_password, encrypt_password
from app.models.user import User
from app.schemas.user_schema import HuaweiCredentialsUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.put("/huawei-credentials", response_model=UserResponse)
def update_huawei_credentials(
    credentials: HuaweiCredentialsUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user = current_user
    user.huawei_username = credentials.huawei_username
    user.huawei_password_encrypted = encrypt_password(credentials.huawei_password)

    db.commit()
    db.refresh(user)
    return user


@router.get("/me/huawei-credentials", response_model=HuaweiCredentialsUpdate)
def get_huawei_credentials(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user or not user.huawei_username:
        raise HTTPException(status_code=404, detail="Huawei credentials not found")

    return HuaweiCredentialsUpdate(
        huawei_username=user.huawei_username,
        huawei_password=decrypt_password(user.huawei_password_encrypted),
    )
