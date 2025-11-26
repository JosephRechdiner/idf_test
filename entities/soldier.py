class Soldier:
    def __init__(self, personal_number: int, first_name: str, last_name: str, gender: str, city: str, distance: int):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance = distance
        self.has_room = False

    def set_has_room(self) -> None:
        self.has_room = True

    def reset_has_room(self) -> bool | None:
        if not self.does_have_room:
            return False
        self.has_room = False

    def does_have_room(self) -> bool:
        return self.has_room