from pygame import Vector2

import core
from Astéroide_CI.player import Player


class Map:
    def __init__(self):
        self.maxPlayer = 1
        self.maxAsteroide = 5
        self.maxSoucoupe = 2
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueur = Player()
        self.aste = []
        self.soucoupe = []

    def spawn_asteroide(self):
        pass

    def spawn_soucoupe(self):
        pass
    def show(self):
        self.joueur.show()


