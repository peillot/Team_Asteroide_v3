import random

from pygame import Vector2

import core


class Player:
    def __init__(self):
        self.nom: "Zizou"
        self.vMax = 10
        self.accMax = 5
        self.taille = 35
        self.position = Vector2(280,200)
        self.acc = Vector2(0,0)
        self.vitesse = Vector2 (0,0)
        self.color = (255,255,255)
        # self.score

    def deplacement(self):
        pass

    def tirer(self):
        pass

    def comptage(self):
        pass

    def show(self):
        core.Draw.text(self.color, "A", self.position, self.taille)
