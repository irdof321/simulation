import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Gèl ou si",quit_key=pyxel.KEY_Q, fps=60)
        pyxel.load( "pyxel_examples/assets/jump_game.pyxres" )
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(10, 10, 20, 20, 11)