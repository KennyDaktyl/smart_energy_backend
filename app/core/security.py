from datetime import datetime, timedelta, timezone

from cryptography.fernet import Fernet
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fernet = Fernet(
    settings.FERNET_KEY.encode() if isinstance(settings.FERNET_KEY, str) else settings.FERNET_KEY
)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7


# -----------------------
# 🔒 PASSWORD HANDLING
# -----------------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
        plain_password = password_bytes.decode("utf-8", errors="ignore")
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
        password = password_bytes.decode("utf-8", errors="ignore")
    return pwd_context.hash(password)


# -----------------------
# 🔑 JWT TOKENS
# -----------------------
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=ALGORITHM)


def create_refresh_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = data.copy()
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=ALGORITHM)


def decode_token(token: str):
    from jose import ExpiredSignatureError

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        print(f"✅ JWT decoded: {payload}")
        return payload
    except ExpiredSignatureError:
        print("⚠️ JWT expired")
    except JWTError as e:
        print(f"❌ JWT decode failed: {e}")
    return None


# -----------------------
# 🔐 HUAWEI CREDENTIALS
# -----------------------
def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
