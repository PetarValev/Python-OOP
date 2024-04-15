class Cup:
    def __init__(self, size: int, filled_quantity: int):
        self.size = size
        self.quantity = filled_quantity

    def fill(self, quantity):
        if self.size >= self.quantity + quantity:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity


cup1 = Cup(100, 50)

cup1.fill(39)
print(cup1.status())