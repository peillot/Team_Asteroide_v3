import random

from pygame import Vector2

import core
from boids.boid import colorFamily

class Player:
    def __init__(self):
        self.nom: "Zizou"
        self.vMax = 10
        self.accMax = 5
        self.taille = 35
        self.pos = Vector2()
        self.acc = Vector2()
        self.vitesse = Vector2 (0,-1)
        self.color = (255,255,255)
        self.angle = 2
        # self.score

    def deplacement(self):
        if core.getKeyPressList("a"):
            self.acc = Vector2(0.5,0)
            self.vitesse +=self.acc
            self.pos += self.vitesse
            print("appuie")

        if core.getKeyPressList("z"):
            self.acc = Vector2(-0.5,0)
            self.vitesse +=self.acc
            self.pos += self.vitesse
            print("appuie")

        if core.getKeyPressList("m"):
            self.acc = Vector2(0,-2)
            self.vitesse +=self.acc
            self.pos += self.vitesse
            print("appuie")

    def tirer(self):
        pass

    def comptage(self):
        pass

    def show(self):
        self.pos = Vector2(280,220)
        p1 =  self.vitesse.rotate(90)
        p1.scale_to_length(10)
        p1+= self.pos
        p3 = self.vitesse.rotate(-90)
        p3.scale_to_length(10)
        p3+=self.pos
        p2 = Vector2(self.vitesse)
        p2.scale_to_length(20)#Sommet du triangle
        p2+=self.pos

        core.Draw.polygon(self.color,((p1), (p2), (p3)))

