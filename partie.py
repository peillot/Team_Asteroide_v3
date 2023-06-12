
from map import Map
from player import Player


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
