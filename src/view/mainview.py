import pyxel

class MainView:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        pyxel.init(256, 256)

    def draw(self):
        pyxel.cls(0)
        for obj in self.data_manager.get_objects():
            img = obj.draw()
            pyxel.blt(img.x, img.y, img.bank, img.u, img.v, img.width, img.height, 0)
        pyxel.flip()

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        pass  # Update logic can go here
