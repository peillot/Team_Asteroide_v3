from agario.Map import Map
from agario.player import Player


class Partie:
    def __init__(self):
        self.map=Map()

    def control(self):
        pass

    def addPlayer(self):
        p=Player()
        p.bot=False
        self.map.addJoueur(p)

    def addBots(self):
        for i in range(0,self.map.maxPlayer):
            self.map.addJoueur(Player())


    def show(self):
        self.map.show()


