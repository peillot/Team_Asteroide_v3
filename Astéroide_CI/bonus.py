import time

from pygame import Vector2
import core


class Bonus:
    def __init__(self, x=0, y=0):
        self.rayon = 30
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.accMax = 1
        self.vitesseMax = 1
        self.position = Vector2(x, y)
        self.dureeDeVie = 3
        self.startTime = time.time()

    def show(self):
        core.memory("texture", core.Texture("./coeur_vie.png", self.position, 0, (40, 40)))
        if not core.memory("texture").ready:
            core.memory("texture").load()
            core.memory("texture").show()

        if self.position.x<0: #Teleporter a droite
            self.position.x = 800

        if self.position.x>800: #Teleporter a gauche
            self.position.x = 0

        if self.position.y<0: #Teleporter en bas
            self.position.y = 500

        if self.position.y>500: #Teleporter en haut
            self.position.y = 0

    def deplacement(self):
        if self.acc.length() > self.accMax:
            self.acc.scale_to_length(self.accMax)
        if self.vitesse.length() > self.vitesseMax:
            self.vitesse.scale_to_length(self.vitesseMax)

        self.vitesse += self.acc

        self.position += self.vitesse
    def collision(self, joueur):
        dist = self.position.distance_to(joueur.pos)
        if dist < self.rayon:
            return True
        return False