from passlib.hash import bcrypt
import hashlib

def _normalize_password(password: str) -> str:
    """
    Bcrypt limit = 72 byte.
    Kalau password lebih panjang, pakai sha256 hexdigest dulu.
    """
    if len(password.encode("utf-8")) > 72:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    return password

def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    return bcrypt.hash(normalized)

def verify_password(password: str, hashed: str) -> bool:
    normalized = _normalize_password(password)
    return bcrypt.verify(normalized, hashed)

def GetEnv(env, senv):
    if env:
        return env
    else:
        return senv