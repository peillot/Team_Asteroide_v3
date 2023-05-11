import random

from pygame import Vector2

import core
from boids.boid import colorFamily

class Player:
    def __init__(self, j="J0", x=10, y=300):
        self.nom: j
        self.vMax = 10
        self.accMax = 5
        self.taille = 35
        self.pos = Vector2(x,y)
        self.acc = Vector2()
        self.vitesse = Vector2()
        self.orientation = Vector2(0, -1) #permet de dessiner le triangle et pouvoir deplacer le joueur
        self.frottement = Vector2()
        self.color = (255,255,255)
        # self.score

    def deplacement(self):
        if core.getKeyPressList("a"): #Tourner a gauche
            self.orientation = self.orientation.rotate(2)
            print("appuie a")

        if core.getKeyPressList("z"): #Tourner a droite
            self.orientation = self.orientation.rotate(-2)
            print("appuie z")

        if core.getKeyPressList("m"): #Avancer
            self.acc = Vector2(self.orientation)
            #print("appuie m")

        self.frottement = self.orientation * -0.03 *self.vitesse.length()
        self.acc += self.frottement
        self.vitesse += self.acc
        self.pos += self.vitesse
        print(self.vitesse, self.acc, self.frottement)

    def tirer(self):
        pass

    def comptage(self):
        pass

    def show(self):
        #self.pos = Vector2(280,220)
        p1 =  self.orientation.rotate(90)
        p1.scale_to_length(10)
        p1+=self.pos
        p3 = self.orientation.rotate(-90)
        p3.scale_to_length(10)
        p3+=self.pos
        p2 = Vector2(self.orientation)
        p2.scale_to_length(20)#Sommet du triangle
        p2=self.pos+p2

        core.Draw.polygon(self.color,((p1), (p2), (p3)))

