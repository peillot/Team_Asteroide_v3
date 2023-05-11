from pygame import Vector2

import core


class Comete:

    def __init__(self):
        self.taille1 = 30
        self.taille2 = 20
        self.taille3 = 10
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.position = Vector2()
        self.dureeDeVie = 3

    def collide(self):
        pass

    def deplacement(self):
        self.vitesse += self.acc
        self.position += self.vitesse

    def draw(self):
        core.Draw.circle((88,41,0), self.position, self.taille1)
