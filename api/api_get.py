import os

from fastapi import APIRouter
from starlette.responses import FileResponse

from conn.db_conn import engineconn
from conn.db_class import Test

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR,'static\\')
IMG_DIR = os.path.join(STATIC_DIR,'images\\')
SERVER_IMG_DIR = os.path.join('http://localhost:8000/','static/','images/')

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

@router.get("/",tags=["get"])
async def first_get():
    example = session.query(Test).all()
    return example


@router.get('/images/{file_name}')
def get_image(file_name:str):
    return FileResponse(''.join([IMG_DIR,file_name]))