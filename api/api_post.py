import os
import secrets
from typing import List

from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from conn.db_conn import engineconn
from conn.db_class import Test
from datetime import datetime

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR,'static\\')
IMG_DIR = os.path.join(STATIC_DIR,'images\\')
SERVER_IMG_DIR = os.path.join('http://localhost:8000/','static/','images/')

class Item(BaseModel):
    name: str
    number: int

@router.post("/post",tags=["post"]  )
async def first_post(item: Item):
    addMemo = Test(name=item.name, number=item.number)
    session.add(addMemo)
    session.commit()
    return item

@router.post("/upload-images")
async def create_upload_file(in_files: List[UploadFile] = File(...)):
    file_urls = []
    for file in in_files:
        saved_file_name = ''.join(["test", secrets.token_hex(16)])
        print(saved_file_name)
        file_location = os.path.join(IMG_DIR, saved_file_name)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        file_urls.append(SERVER_IMG_DIR + saved_file_name)
    result = {'fileUrls': file_urls}
    return result


