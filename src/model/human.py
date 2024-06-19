from .object import Moveable
from .object import Gatherable
import pyxel

class Human(Moveable):
    def __init__(self, id: int, position: tuple, size: tuple, name: str, age: int, bank: int = 0, u: int = 0, v: int = 0):
        super().__init__(id, position, size, bank, u, v)
        self.name = name
        self.age = age
        self.inventory = []

        # Load the human sprite from the pyxres file
        pyxel.images[self.id].load(0, 0, "assets/human.pyxres")

    def move(self):
        print(f"{self.name} is moving.")

    def gather(self, gatherable: Gatherable):
        print(f"{self.name} is gathering {gatherable}.")
        self.inventory.append(gatherable)

    def draw(self):
        return super().draw()