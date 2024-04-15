class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int):
        if self.content + ml <= Glass.capacity:
            self.content += ml
            return f"Glass filled with {self.content} ml"

        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        free_space = Glass.capacity - self.content
        return f"{free_space} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
