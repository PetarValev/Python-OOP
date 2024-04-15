from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room_number: int):
        self.rooms.append(room_number)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_name: str):
        room = [r for r in self.rooms if r.number == room_name][0]
        room.free_room()

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
                f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")
