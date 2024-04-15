from project.animal import Animal


class Dog(Animal):
    def bark(self) -> str:
        return "barking..."


pincher = Dog()
print(pincher.eat())
print(pincher.bark())