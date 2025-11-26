from fastapi import APIRouter, HTTPException, Depends 
from fastapi import UploadFile, File
from csv_handler import convert_csv_to_objects
from utils import sorting_soldiers
from entities.manager import HouseInserter
from entities.manager import HouseManager

upload_file_router = APIRouter()

@upload_file_router.post("/assignWithCsv")
def upload_csv(file: UploadFile = File(...)):
    soldiers = convert_csv_to_objects(file)
    sorted_soldiers = sorting_soldiers(soldiers)
    wanting = HouseInserter.insert_soldiers_to_house(sorted_soldiers)
# inserted, not_inserted 
    return wanting