from fastapi import APIRouter
from conn.db_conn import engineconn
from conn.db_class import Test

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

@router.get("/",tags=["get"])
async def first_get():
    example = session.query(Test).all()
    return example