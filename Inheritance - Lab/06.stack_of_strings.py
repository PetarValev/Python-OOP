from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        reversed_data = self.data[::-1]
        return f"[{', '.join(reversed_data)}]"


