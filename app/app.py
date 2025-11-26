from fastapi import FastAPI
from app.routs.csv_router import upload_file_router

app = FastAPI()

app.include_router(upload_file_router, prefix="/file")