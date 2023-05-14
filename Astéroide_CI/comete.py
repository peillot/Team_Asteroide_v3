import random

from pygame import Vector2

import core


class Comete:

    def __init__(self, x=0, y=0):
        self.rayon = 40
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.accMax = 2
        self.vitesseMax = 1
        self.position = Vector2(x,y)
        self.dureeDeVie = 3

    def collision_projectile(self, projectile):
        dist = self.position.distance_to(projectile.position)
        if dist<self.rayon:
            return True
        return False
    def collision_joueur(self, joueur):
        dist = self.position.distance_to(joueur.pos)
        if dist < self.rayon:
            return True
        return False

    def deplacement(self):
        if self.acc.length()>self.accMax:
            self.acc.scale_to_length(self.accMax)
        if self.vitesse.length()>self.vitesseMax:
            self.vitesse.scale_to_length(self.vitesseMax)

        self.vitesse += self.acc

        self.position += self.vitesse

    def draw(self):

        #core.memory("texture", core.Texture("./asteroide_image.png", self.position, 0, (130,130)))
        #if not core.memory("texture").ready:
         #   core.memory("texture").load()
          #  core.memory("texture").show()
        core.Draw.circle((96,96,96), self.position, self.rayon) # Dessin d'asteroide

        if self.position.x<0: #Teleporter a droite
            self.position.x = 800

        if self.position.x>800: #Teleporter a gauche
            self.position.x = 0

        if self.position.y<0: #Teleporter en bas
            self.position.y = 500

        if self.position.y>500: #Teleporter en haut
            self.position.y = 0