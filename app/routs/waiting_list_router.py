from fastapi import APIRouter, Depends
from entities.house import House, get_house
from entities.manager import HouseManager
from entities.waiting_list import WatingList

waiting_list_router = APIRouter()

@waiting_list_router.get("/space")
def get_wating_list():
    return {"full_rooms_total": WatingList.get_all_soldier()}