from soldier import Soldier

class Room:
    def __init__(self, max_soldiers_capacity=8):
        self.soldiers = []
        self.max_soldiers_capacity = max_soldiers_capacity

    def add_soldier(self, soldier: Soldier) -> bool | None:
        if not self.enough_capacity_for_adding:
            return False
        self.soldiers.append(soldier)

    def remove_soldier(self, soldier_to_remove: Soldier) -> bool | None:
        if not self.has_no_soldiers:
            return False
        self.soldiers = [soldier for soldier in self.soldiers if soldier != soldier_to_remove]

    def enough_capacity_for_adding(self):
        return len(self.soldiers) <= 8
    
    def has_no_soldiers(self):
        return len(self.soldiers) >= 0
    
