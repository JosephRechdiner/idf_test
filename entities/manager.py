from entities.house import House
from entities.soldier import Soldier
from entities.dorm import Dorm
from entities.room import Room
from entities.waiting_list import WatingList

class HouseManager:

    def create_house():
        return House()

    def add_dorm_to_house(house: House):
        return house.add_dorm()

    def add_room_to_dorm(dorm: Dorm):
        return dorm.add_room()

    def add_soldier_to_room(soldier: Soldier, room: Room):
        room.add_soldier(soldier)

    def add_soldier_to_wating_list(wating_list: WatingList, soldier: Soldier):
        wating_list.add_soldier(soldier)

    def show_soldiers(house):
        return house.get_all_soldiers()
    
    def show_amount_full_rooms(house):
        return house.get_amount_full_rooms()
    
    def show_amount_empty_rooms(house):
        return len(house.get_amount_empty_rooms())

    def show_amount_not_empty_not_full_rooms(house):
        return len(house.get_amount_full_rooms())
    
    def show_wating_list(house):
        return house.


class HouseInserter:
    def insert_soldiers_to_house(soldiers: list[Soldier]):
        inserted = []
        not_inserted = []

        house = HouseManager.create_house()
        dorm_to_insert = HouseManager.add_dorm_to_house(house)
        room_to_insert = HouseManager.add_room_to_dorm(dorm_to_insert)
        wating_list = WatingList()

        max_soldiers_per_house = house.max_dorms_capacity * dorm_to_insert.max_rooms_capacity * room_to_insert.max_soldiers_capacity
        max_soldiers_per_dorm = dorm_to_insert.max_rooms_capacity * room_to_insert.max_soldiers_capacity
        max_soldiers_per_room = room_to_insert.max_soldiers_capacity

        first_not_inserted_soldier_idx = 0
        for i in range(len(soldiers)):
            if i == max_soldiers_per_house:
                first_not_inserted_soldier_idx = i
                break

            if i % max_soldiers_per_dorm == 0:
                dorm_to_insert = HouseManager.add_dorm_to_house(house)

            if i % max_soldiers_per_room == 0:
                room_to_insert = HouseManager.add_room_to_dorm(dorm_to_insert)

            HouseManager.add_soldier_to_room(soldiers[i], room_to_insert)
            inserted.append({
                "details": soldiers[i],
                "has_room": "Yes!",
                "dorm_number": dorm_to_insert.dorm_id,
                "room_number": room_to_insert.room_id
                })
                 
        for i in range(first_not_inserted_soldier_idx, len(soldiers)):
            not_inserted.append({
                "details": soldiers[i],
                "has_room": "No!",
                })
            HouseManager.add_soldier_to_wating_list(wating_list, soldiers[i])

        return inserted, not_inserted
    

            



            

        