import pyxel
import random

class Personnage:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1])  # Vitesse horizontale initiale aléatoire
        self.dy = random.choice([-1, 1])  # Vitesse verticale initiale aléatoire
        self.update_counter = 0
        pyxel.image(0).load(0, 0, image_path)

    def update(self):
        self.update_counter += 1

        # Changer la direction de manière aléatoire toutes les 30 mises à jour
        if self.update_counter % 30 == 0:
            self.dx = random.choice([-1, 1])
            self.dy = random.choice([-1, 1])

        self.x += self.dx
        self.y += self.dy

        # Détection des bords de l'écran et inversion de la direction
        if self.x < 0 or self.x + 16 > pyxel.width:
            self.dx *= -1
        if self.y < 0 or self.y + 16 > pyxel.height:
            self.dy *= -1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)

class Jeu:
    def __init__(self):
        pyxel.init(160, 120, title="Jeu avec Personnage")
        self.personnage = Personnage(50, 50, "personnage.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.personnage.update()

    def draw(self):
        pyxel.cls(0)
        self.personnage.draw()

if __name__ == "__main__":
    Jeu()
