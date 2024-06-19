from abc import ABC, abstractmethod

class Image:
    def __init__(self, x, y, width, height, bank, u, v):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bank = bank
        self.u = u
        self.v = v

class Object(ABC):
    def __init__(self, id: int, position: tuple, size: tuple, bank: int, u: int, v: int):
        self.id = id
        self.position = position
        self.size = size
        self.bank = bank
        self.u = u
        self.v = v

    @abstractmethod
    def draw(self):
        return Image(self.position[0], self.position[1], self.size[0], self.size[1], self.bank, self.u, self.v)

class Static(Object):
    pass

class Gatherable(Object, ABC):
    def __init__(self, id: int, position: tuple, size: tuple, bank: int, u: int, v: int, nutrition_value: int):
        super().__init__(id, position, size, bank, u, v)
        self.nutrition_value = nutrition_value

    @abstractmethod
    def gather(self):
        pass

class Moveable(Object, ABC):
    @abstractmethod
    def move(self):
        pass