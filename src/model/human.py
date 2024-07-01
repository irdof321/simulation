from .object import Moveable
from .object import Gatherable
import pyxel

class Human(Moveable):
    def __init__(self, id: int, position: tuple, size: tuple, name: str, age: int):
        super().__init__(id, position, size, bank, u, v)
        self.name = name
        self.age = age
        self.inventory = []

    def move(self):
        print(f"{self.name} is moving.")

    def gather(self, gatherable: Gatherable):
        print(f"{self.name} is gathering {gatherable}.")
        self.inventory.append(gatherable)

    def draw(self):
        pyxel.blt(self.position[0], self.position[1],0,0,0, self.size[0], self.size[1], 0)