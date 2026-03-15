
from fastapi import APIRouter, Depends
from requests import Session
from app.auth.dependency import get_current_user
from app.auth.models import Users
from app.database.database import get_db
from app.todo.schemas import CreateTodoRequet,CreateTodoResponse
from app.todo.servics import create_todo, get_user_todo


router=APIRouter(prefix="/todo",tags=["ToDo"])




@router.post("/create")
def createtodo(
    todo: CreateTodoRequet,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)):

    return create_todo(db, todo, current_user.id)


@router.get("/get_todo")
def get_user(db:Session=Depends(get_db),current_user:Users=Depends(get_current_user)):
    return get_user_todo(db,current_user.id)



