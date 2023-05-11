import core
from Astéroide_CI.comete import Comete
from Astéroide_CI.map import Map
from Astéroide_CI.player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.joueur = Player("J1", 400,250)


    def control(self):
        self.joueur.deplacement()


    def show(self):
        self.joueur.show()
        self.map.show()
        #self.map.spawn_asteroide()