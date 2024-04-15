from typing import List
from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, customer_id: int) -> None:
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds: List[DVD] = []

    def __repr__(self) -> str:
        return (f"{id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})")
