from fastapi import FastAPI
from app.routs.csv_router import upload_file_router
from app.routs.space_router import space_router
from app.routs.waiting_list_router import waiting_list_router

app = FastAPI()

app.include_router(upload_file_router, prefix="/file")
app.include_router(space_router, prefix="/space")
app.include_router(waiting_list_router, prefix="/wating_list")