from house import House
from soldier import Soldier
from dorm import Dorm
from room import Room

class HouseManager:
    def __init__(self):
        self.house = House()
        self.dorms = [self.house.add_dorm(Dorm()) for i in range(len(self.house.max_dorms_capacity))]
        self.rooms = [self.dorms.add_room(Room())]

    def create_house(self):
        pass

    def add_dorms(self):
        for i in range(len(self.house.max_dorms_capacity)):
            new_dorm = Dorm()
            self.house.add_dorm(new_dorm)

    def add_rooms(self):
        pass

