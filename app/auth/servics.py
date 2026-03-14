from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.auth.models import Users 
from app.auth.schemas import CreateUsersRequest
from app.auth.models import Users

from app.auth.security import hash_password,verify_password,create_access_token



#create User(signup )

def create_user(db:Session,username:str,email:str,password:str,phone_number:str):

    existing_user = db.query(Users).filter(Users.email == email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Users All Ready Registered")
    
    new_user=Users(
        username=username,
        email=email,
        hashed_password=hash_password(password),
        phone_number=phone_number
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


#Authenticate User (Login) 
def authenticate_user(db:Session,email:str,password:str):

    user=db.query(Users).filter(email==Users.email).first()

    if not user:
       return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    return user


# Login users 

def login_user(db:Session,email:str,password:str):

    user=authenticate_user(db,email,password)

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    
    token = create_access_token(user.id)
    return {"access_token":token,"token_type":"bearer"}
        



# Get User By ID
def get_user_by_id(db: Session, user_id: int):
    user = db.query(Users).filter(Users.id == user_id).first()
    return user