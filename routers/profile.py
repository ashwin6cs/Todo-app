from fastapi import APIRouter, HTTPException, status, Form, UploadFile, File
from gridfs import GridFS
from config.database import db
from common.common import check_user_name_existence
from gridfs.errors import FileExists
from fastapi.responses import StreamingResponse
from bson import ObjectId

profile_router = APIRouter()

profile_pictures = {}

@profile_router.post('/upload_profile_pic')
async def upload_profile_pic(user_name: str = Form(...), profile_picture: UploadFile = File(...)):

    if not check_user_name_existence(user_name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found")
    
    try:
        fs = GridFS(db, "profile_pic")
        file_id = fs.put(profile_picture.file.read(), filename=profile_picture.filename, user_name=user_name)
        return {'file_id': str(file_id)}
    except FileExists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File for this user id already exists")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@profile_router.get('/get_profile_pic/{file_id}')
async def get_profile_pic(file_id: str):
    try:
        fs = GridFS(db, "profile_pic")
        file_data = fs.get(ObjectId(file_id))
        if not file_data:
            raise HTTPException(status_code=404, detail='Profile picture not found')
        return StreamingResponse(file_data, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
