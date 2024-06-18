from object import Object

class Static(Object):
    def __init__(self, id: int, position: tuple):
        super().__init__(id, position)
    
    def get_position(self):
        return self.position
