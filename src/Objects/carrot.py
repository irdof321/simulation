from static import Static
from gatherable import Gatherable

class Carrot(Static, Gatherable):
    def __init__(self, id: int, position: tuple, nutritional_value: int):
        super().__init__(id, position)
        self.nutritional_value = nutritional_value

    def gather(self):
        print("Carrot is being gathered.")
