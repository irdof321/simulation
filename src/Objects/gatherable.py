from abc import ABC, abstractmethod
from object import Object

class Gatherable(Object, ABC):
    @abstractmethod
    def gather(self):
        pass
