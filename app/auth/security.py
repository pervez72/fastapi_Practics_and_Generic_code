from passlib.context import CryptContext
from fastapi import exceptions,HTTPException,status



bcrypt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


# hashed password
def hash_password(password:str):
    return bcrypt_context.hash(password)

# verify password 
def verify_password(password:str,hashed_password:str):
    return bcrypt_context.verify(password,hashed_password)


#create Access Token 
import jwt 
from datetime import datetime,timedelta

SECRET_KEY = "08f710f26a62a6a2d253005bcfbe6a4bfb0856b65a1681fcc9bb8653d67b895c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(user_id:int):
    payload={
        "user_id":user_id,
        "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    return token


# Verify JWT Token 
def verify_token(token:str):
    try:
        payload=jwt.decode(payload,SECRET_KEY,algorithms=[ALGORITHM])
        
        user_id=payload.get(user_id)

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token"
            )
        return user_id
    
    except jwt.ExpiredSignatureError:
           raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalid"
        )