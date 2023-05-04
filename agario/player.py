import random

from pygame import Vector2

import core


class Player:
    def __init__(self):
        self.bot=True
        self.name="Bob"
        self.uuid=random.randint(1000000,99999999)
        self.mass=10
        self.vMax=10
        self.accMax=5
        self.position=Vector2(random.randint(0,core.WINDOW_SIZE[0]), random.randint(0,core.WINDOW_SIZE[1]))
        self.acc = Vector2(0, 0)
        self.vitesse = Vector2(0, 0)
        self.couleur =(random.randint(0,200),random.randint(0,200), random.randint(0,200))


    def deplacement(self):
        if self.bot== False:
            if core.getMouseRightClick():
            k=0.01
            u=1
            l=
            lo=0.01
            Fa=k*u*(l-lo)
            self.acc=Fa
            self.vitesse=self.vitesse+self.acc
            self.position=self.position+self.vitesse


    def grandir(self):
        pass

    def evaporation(self):
        pass

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.mass)





