class DataManager:
    def __init__(self):
        self.gatherables = []
        self.moveables = []
        self.humans = []

    def add_gatherable(self, gatherable):
        self.gatherables.append(gatherable)

    def add_moveable(self, moveable):
        self.moveables.append(moveable)

    def add_human(self, human):
        self.humans.append(human)

    def get_objects(self):
        return self.gatherables + self.moveables + self.humans
