from Astéroide_CI.map import Map
from Astéroide_CI.player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.joueur = Player()

    def control(self):
        self.joueur.deplacement()
        self.joueur.show()


    def show(self):
        pass