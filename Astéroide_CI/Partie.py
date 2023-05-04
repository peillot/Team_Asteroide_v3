from Astéroide_CI.map import Map
from Astéroide_CI.player import Player


class Partie:
    def __init__(self):
        self.map = Map()

    def control(self):
        pass

    def show(self):
        self.map.show()