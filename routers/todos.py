from fastapi import APIRouter, HTTPException, status, Form, UploadFile, File
from models.todo import Todo
from config.database import todo_collection
from schema.schemas import list_documents_serial
from bson import ObjectId

todo_router = APIRouter()

@todo_router.get("/gettodo")
async def get_todos():
    todos_cursor = todo_collection.find()
    todos_list = list_documents_serial(todos_cursor, "todo")
    return {"todos": todos_list, "total": len(todos_list)}

@todo_router.post("/posttodo", response_model=Todo)
async def post_todo(todo: Todo):
    try:
        result = todo_collection.insert_one(dict(todo))
        inserted_id = result.inserted_id
        inserted_todo = todo_collection.find_one({"_id": inserted_id})
        return Todo(**inserted_todo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@todo_router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    result = todo_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(todo)},
        return_document=True
    )
    if result:
        return {"message": f"Todo with id {id} updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found")

@todo_router.delete("/deletetodo/{id}")
async def delete_todo(id: str):
    result = todo_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": f"Todo with id {id} deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found")
