import core
from Astéroide_CI.comete import Comete
from Astéroide_CI.map import Map
from Astéroide_CI.player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.joueur = Player("J1", 280,220)


    def control(self):
        self.joueur.deplacement()
        self.joueur.show()

    def show(self):
        self.map.spawn_asteroide()