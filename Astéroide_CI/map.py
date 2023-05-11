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
        pass

    def spawn_soucoupe(self):
        pass
    def show(self):
        core.Draw.rect((255, 0, 0), (0, 510, 800, 5))  # Zone Spawn en bas
        core.Draw.rect((255, 0, 0), (0, -10, 800, 5))  # Zone Spawn en haut
        core.Draw.rect((255, 0, 0), (-10, 0, 5, 500))  # Zone Spawn a gauche
        core.Draw.rect((255, 0, 0), (810, 0, 5, 500))  # Zone Spawn a droite

        core.Draw.rect((0, 255, 0), (0, 520, 800, 40))  # Zone Teleportation en bas
        core.Draw.rect((0, 255, 0), (0, -50, 800, 40))  # Zone Teleportation en haut
        core.Draw.rect((0, 255, 0), (-50, 0, 40, 500))  # Zone Teleportation a gauche
        core.Draw.rect((0, 255, 0), (820, 0, 40, 500))  # Zone Teleportation a droite


