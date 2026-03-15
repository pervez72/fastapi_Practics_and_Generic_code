from fastapi import APIRouter,Depends
from app.auth.schemas import CreateUsersRequest,LoginRequest
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.auth.servics import create_user,login_user
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(prefix="/auth",tags=["Authentication"])



# User signup
@router.put("/register")
def register_user(user:CreateUsersRequest,db:Session=Depends(get_db)):
    
    return create_user(
        db,
        username=user.username,
        email=user.email,
        password=user.password,
        phone_number=user.phone_number
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        db=db,
        email=form_data.username,   # username field → email
        password=form_data.password
    )
