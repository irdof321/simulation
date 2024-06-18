from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, id: int, position: tuple):
        self.id = id
        self.position = position

    def get_position(self):
        return self.position
