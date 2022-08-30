from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__= "test"
    id = Column(BIGINT,nullable=False,autoincrement=True,primary_key=True)
    name = Column(TEXT,nullable=False)
    number = Column(INT, nullable=False)

class FileServer(Base):
    __tablename__= "filelist"
    file_id = Column(BIGINT,nullable=False,autoincrement=True,primary_key=True)
    file_name = Column(TEXT,nullable=False)
    file_path = Column(TEXT,nullable=False)
