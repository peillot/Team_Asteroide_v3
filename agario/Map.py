from pygame import Vector2

import core


class Map:

    def __init__(self):
        self.maxPlayer=200
        self.maxFoof=100
        self.taille=Vector2(core.WINDOW_SIZE)
        self.joueur=[]
        self.food=[]
        self.pièges=[]

    def spawn_food(self):
        pass

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueur:
            j.show()
            
    def addJoueur(self,p):
        if len(self.joueur)<self.maxPlayer:
            self.joueur.append(p)


