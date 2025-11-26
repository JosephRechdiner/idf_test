from dorm import Dorm

class House:
    def __init__(self, max_dorms_capacity=2):
        self.dorms = []
        self.max_dorms_capacity = max_dorms_capacity

    def add_dorm(self) -> bool | None:
        if not self.enough_capacity_for_adding:
            return False
        new_dorm = Dorm()
        self.dorms.append(new_dorm)

    def remove_dorm(self, dorm_to_remove: Dorm) -> bool | None:
        if not self.has_dorms:
            return False
        self.dorms = [dorm for dorm in self.dorms if dorm != dorm_to_remove]

    def enough_capacity_for_adding(self) -> bool:
        return len(self.dorms) < self.max_dorms_capacity
    
    def has_dorms(self) -> bool:
        return len(self.dorms) > 0