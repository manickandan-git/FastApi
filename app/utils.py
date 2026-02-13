from passlib.context import CryptContext
import hashlib
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    sha256_hash = hashlib.sha256(password.encode('utf-8')).digest()
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(sha256_hash, salt)
    
    # Decode to UTF-8 string so it can be stored in a DB VARCHAR column
    return hashed_bytes.decode('utf-8')

def verify(plain_password: str, hashed_password: str):
    # 1. Convert the plain password to SHA-256
    sha256_hash = hashlib.sha256(plain_password.encode('utf-8')).digest()
        
    # 2. Clean the hash (remove accidental whitespace) and encode
    db_bytes = hashed_password.strip().encode('utf-8')
    
    # 3. Verify
    return bcrypt.checkpw(sha256_hash, db_bytes)

