import pytest

from app.todo.servics import create_todo, get_user_todo
from app.todo.schemas import CreateTodoRequet


@pytest.fixture
def todo_request():
    return CreateTodoRequet(
        title="Test Todo",
        description="Testing todo",
        completed=True,
        priority=1,
    )


def test_create_todo(db_session, todo_request):
    user_id = 1
    todo = create_todo(
        db=db_session,
        create_todo=todo_request,
        user_id=user_id
    )
    
    assert todo.id is not None
    assert todo.title == "Test Todo"
    assert todo.description == "Testing todo"
    assert todo.priority == 1
    assert todo.completed is True
    assert todo.owner_id == user_id