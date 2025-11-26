from entities.soldier import Soldier

class WatingList:
    def __init__(self):
        self.soldiers = []

    def add_soldier(self, soldier: Soldier) -> None:
        # Based on: no limit capacity
        self.soldiers.append(soldier)

    def remove_soldier(self, soldier_to_remover: Soldier) -> bool | None:
        if not self.has_soldiers:
            return False
        self.soldiers = [soldier for soldier in self.soldiers if soldier != soldier_to_remover]

    def has_soldiers(self) -> bool:
        return len(self.soldiers)
    
    def get_all_soldier(self):
        return self.soldiers