from requests import Session

from app.todo.models import ToDo
from app.todo.schemas import CreateTodoRequet,CreateTodoResponse


def create_todo(db:Session,create_todo:CreateTodoRequet,user_id:int):
    new_todo=ToDo(
        title=create_todo.title,
        description=create_todo.description,
        priority=create_todo.priority,
        owner_id=user_id
    )
    
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


# Get user todo
def get_user_todo(db:Session,user_id:int):
    todos=db.query(ToDo).filter(ToDo.owner_id==user_id).all()

    return todos