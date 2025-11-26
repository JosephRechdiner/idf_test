from entities.soldier import Soldier

class Room:
    room_id = 0
    
    def __init__(self, max_soldiers_capacity=8):
        self.soldiers = []
        self.max_soldiers_capacity = max_soldiers_capacity
        self.room_id = Room.room_id

        Room.room_id += 1

    def add_soldier(self, soldier: Soldier) -> bool | None:
        if not self.enough_capacity_for_adding:
            return False
        soldier.set_has_room()
        self.soldiers.append(soldier)

    def remove_soldier(self, soldier_to_remove: Soldier) -> bool | None:
        if not self.has_soldiers:
            return False
        soldier_to_remove.reset_has_room()
        self.soldiers = [soldier for soldier in self.soldiers if soldier != soldier_to_remove]

    def enough_capacity_for_adding(self) -> bool:
        return len(self.soldiers) < self.max_soldiers_capacity
    
    def has_soldiers(self) -> bool:
        return len(self.soldiers) > 0
    
    def is_full(self):
        return len(self.soldiers) == self.max_soldiers_capacity
    
    def is_empty(self):
        return len(self.soldiers) == 0
    
    def is_not_full_not_empty(self):
        return not self.is_empty() and not self.is_full()