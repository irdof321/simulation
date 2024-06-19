from .object import Static
from .object import Gatherable
import pyxel

class Carrot(Static, Gatherable):
    def __init__(self, id: int, position: tuple, size: tuple, bank: int = 0, u: int = 16, v: int = 0, nutrition_value: int = 50):
        Gatherable.__init__(self, id, position, size, bank, u, v, nutrition_value)
        Static.__init__(self, id, position, size, bank, u, v)

        # Load the carrot sprite from the pyxres file
        pyxel.images[self.id].load(0, 0, "assets/carrot.pyxres")

    def gather(self):
        print("Carrot is being gathered.")

    def draw(self):
        return super().draw()
