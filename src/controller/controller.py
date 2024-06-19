class Controller:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def update(self):
        for human in self.data_manager.humans:
            human.move()
            for gatherable in self.data_manager.gatherables:
                if self.check_proximity(human, gatherable):
                    human.gather(gatherable)
                    self.data_manager.gatherables.remove(gatherable)

    def check_proximity(self, human, gatherable):
        hx, hy = human.position
        gx, gy = gatherable.position
        distance = ((hx - gx) ** 2 + (hy - gy) ** 2) ** 0.5
        return distance < 10  # Adjust the proximity threshold as needed