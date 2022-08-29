from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from conn.db_conn import engineconn
from conn.db_class import Test

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    name: str
    number: int

@router.post("/post",tags=["post"]  )
async def first_post(item: Item):
    addMemo = Test(name=item.name, number=item.number)
    session.add(addMemo)
    session.commit()
    return item

@router.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


