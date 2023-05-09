from Astéroide_CI.map import Map
from Astéroide_CI.player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.joueur = Player()

    def control(self):
        self.joueur.deplacement()

    def show(self):
        self.map.show()