import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120,title="Exemple de base",quit_key=pyxel.KEY_Q,fps=30)
        pyxel.load("../pyxel_examples/assets/jump_game.pyxres")
        pyxel.run(self.update,self.draw)
    
    # Fonction de mise à jour et appele à chaque frame    
    def update(self):
        pass
    
    # Fonction de dessin et appele à chaque frame (fps)
    def draw(self):
        background_color = 12
        pyxel.cls(background_color)
        
        screnn_top_left_of_sprite = (0,104)
        image_nb = 0
        sprite_coord_in_ressource = (0,0)
        sprite_width_in_ressource = 16
        sprite_height_in_ressource = 16
        color_transparent = 12 # 12 is the color index of the transparent color in the image, 12 = blue
        pyxel.blt(screnn_top_left_of_sprite[0],screnn_top_left_of_sprite[1],
                  image_nb,
                  sprite_coord_in_ressource[0],sprite_coord_in_ressource[1],
                  sprite_width_in_ressource,sprite_height_in_ressource,
                  color_transparent)
                  
                  
        pass
    
App()