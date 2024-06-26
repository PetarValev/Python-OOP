class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, mammal_type: str, sound: str) -> None:
        self.name = name
        self.type = mammal_type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return self.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"

