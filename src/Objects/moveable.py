from abc import ABC, abstractmethod
from object import Object

class Moveable(Object, ABC):
    @abstractmethod
    def move(self):
        pass
