from entities.room import Room

class Dorm:
    dorm_id = 0

    def __init__(self, max_rooms_capacity=10):
        self.rooms = []
        self.max_rooms_capacity = max_rooms_capacity
        self.dorm_id = Dorm.dorm_id

        Dorm.dorm_id += 1

    def add_room(self) -> bool | Room:
        if not self.enough_capacity_for_adding:
            return False
        new_room = Room()
        self.rooms.append(new_room)
        return new_room

    def remove_room(self, room_to_remove: Room) -> bool | None:
        if not self.has_rooms:
            return False
        self.rooms = [room for room in self.rooms if room != room_to_remove]

    def enough_capacity_for_adding(self) -> bool:
        return len(self.rooms) < self.max_rooms_capacity
    
    def has_rooms(self) -> bool:
        return len(self.rooms) > 0
