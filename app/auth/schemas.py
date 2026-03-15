from app.auth.models import Users 
from pydantic import BaseModel

class CreateUsersRequest(BaseModel):
    username:str
    email:str
    password:str
    phone_number:str

class LoginRequest(BaseModel):
    email:str
    password:str

