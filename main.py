from fastapi import FastAPI
from api import api_get
from api import api_post

app = FastAPI()
app.include_router(api_get.router)
app.include_router(api_post.router)
