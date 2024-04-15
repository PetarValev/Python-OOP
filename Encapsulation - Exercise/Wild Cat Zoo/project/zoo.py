from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        budget_is_enough = self.__budget >= price
        capacity_is_enough = self.__animal_capacity > len(self.animals)
        if capacity_is_enough and budget_is_enough:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif not budget_is_enough and capacity_is_enough:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            wanted_worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(wanted_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_money = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            result += f"{l}\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            result += f"{t}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            result += f"{c}\n"

        return result[:-1]

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]

        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{k}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            result += f"{c}\n"

        result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            result += f"{v}\n"

        return result[:-1]



