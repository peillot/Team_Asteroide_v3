import random
import time

from pygame import Vector2

import core

from Astéroide_CI.comete import Comete
from Astéroide_CI.player import Player


class Projectile:
    def __init__(self):
        self.rayon = 5
        self.accMax = 2
        self.vitesseMax = 9
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.position = Vector2()
        self.dureeDeVie = 1.5
        self.startTime = time.time()
        self.comete = Comete()


    def draw(self):
        core.Draw.circle(((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))),self.position, self.rayon)
        #core.Draw.rect((255,0,0), (self.position.x-4,self.position.y-4, 8,8))

        if self.position.x<0: #Teleporter a droite
            self.position.x = 800

        if self.position.x>800: #Teleporter a gauche
            self.position.x = 0

        if self.position.y<0: #Teleporter en bas
            self.position.y = 500

        if self.position.y>500: #Teleporter en haut
            self.position.y = 0

    def deplacement(self):
        if self.acc.length()>self.accMax:
            self.acc.scale_to_length(self.accMax)
        if self.vitesse.length()>self.vitesseMax:
            self.vitesse.scale_to_length(self.vitesseMax)

        self.vitesse += self.acc
        self.position += self.vitesse




