from fastapi import APIRouter, Depends
from entities.manager import HouseManager
from entities.house import House, get_house

space_router = APIRouter()

@space_router.get("/space")
def get_full_rooms(house: House = Depends(get_house)):
    return {"full_rooms_total": HouseManager.show_amount_full_rooms(house)}

def get_half_full_rooms(house: House = Depends(get_house)):
    return {"half_full_rooms_total": HouseManager.show_amount_not_empty_not_full_rooms(house)}

def get_empty_room(house: House = Depends(get_house)):
    return {"empty_rooms_total": HouseManager.show_amount_empty_rooms(house)}