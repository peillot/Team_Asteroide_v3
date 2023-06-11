import random

import core
from Astéroide_CI.comete import Comete
from Astéroide_CI.map import Map
from Astéroide_CI.player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.joueur = Player("J1", 370,210)

    def control(self):
        self.joueur.deplacement()


    def show(self):
        self.map.show()
        self.joueur.show()
        self.joueur.showVie()
