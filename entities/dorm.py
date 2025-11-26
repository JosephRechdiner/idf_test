from room import Room

class Dorm:
    def __init__(self, max_rooms_capacity=10):
        self.rooms = []
        self.max_rooms_capacity = max_rooms_capacity

    def add_room(self, room: Room) -> bool | None:
        if not self.enough_capacity_for_adding:
            return False
        self.rooms.append(room)

    def remove_soldier(self, room_to_remove: Room) -> bool | None:
        if not self.has_rooms:
            return False
        self.rooms = [room for room in self.rooms if room != room_to_remove]

    def enough_capacity_for_adding(self) -> bool:
        return len(self.rooms) < self.max_rooms_capacity
    
    def has_rooms(self) -> bool:
        return len(self.rooms) > 0