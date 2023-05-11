from pygame import Vector2

import core
from Astéroide_CI.comete import Comete
from Astéroide_CI.player import Player


class Map:
    def __init__(self):
        self.maxPlayer = 1
        self.maxAsteroide = 5
        self.maxSoucoupe = 2
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueur = Player()
        self.aste = Comete()
        self.soucoupe = []

    def spawn_asteroide(self):
        self.aste.draw()

    def spawn_soucoupe(self):
        pass
    def show(self):
        pass


