from fastapi import APIRouter

router = APIRouter()


@router.get("/todos/", tags=["todo"])
def get_todos():
    return [
        {"activity": "Walk Dog", "status": "in_progress"},
        {"activity": "Cook Dinner", "status": "todo"}
    ]


@router.get("/todos/{todo_id}/{todo_name}", tags=["todo"])
def get_todo_by_id(todo_id: int, todo_name: int):
    return [
        {"activity": "Walk Dog", "status": "in_progress"},
        {"activity": "Cook Dinner", "status": "todo"}
    ]
