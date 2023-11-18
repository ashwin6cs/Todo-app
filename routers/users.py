from fastapi import APIRouter, HTTPException, status, Form, UploadFile, File
from models.users import Users
from config.database import user_collection
from schema.schemas import list_documents_serial
from pymongo.errors import DuplicateKeyError

user_router = APIRouter()

@user_router.post("/postuser", response_model=Users)
async def post_user(user: Users):
    try:
        result = user_collection.insert_one(dict(user))
        inserted_id = result.inserted_id
        inserted_user = user_collection.find_one({"_id": inserted_id})
        return Users(**inserted_user)
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@user_router.get("/getusers")
async def get_users():
    users_cursor = user_collection.find()  # Assuming user_collection is defined somewhere
    users_list = list_documents_serial(users_cursor, "user")
    return {"users": users_list, "total": len(users_list)}
