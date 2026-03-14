from pydantic import BaseModel


class CreateTodoRequet(BaseModel):
    title:str
    description:str
    priority:int
    completed:bool


class CreateTodoResponse(BaseModel):
    title:str
    description:str
    priority:int
    completed:bool




