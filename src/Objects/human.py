from moveable import Moveable
from gatherable import Gatherable

class Human(Moveable, Gatherable):
    def __init__(self, id: int, position: tuple, name: str, age: int):
        super().__init__(id, position)
        self.name = name
        self.age = age

    def move(self):
        print(f"{self.name} is moving.")

    def gather(self):
        print(f"{self.name} is gathering resources.")
