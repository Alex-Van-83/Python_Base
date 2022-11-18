from fastapi import FastAPI
from redis.views import router as storage_router

app = FastAPI()
app.include_router(storage_router)


