import random

import pygame.transform
from pygame import Vector2

import core


class Player:
    def __init__(self, j="J0", x=10, y=300):
        self.nom: j
        self.vitesseMax = 5
        self.accMax = 3
        self.pos = Vector2(x,y)
        self.acc = Vector2()
        self.vitesse = Vector2(1,0)
        self.orientation = Vector2(0, -1) #permet de dessiner le triangle et pouvoir deplacer le joueur
        self.frottement = Vector2()
        self.color = (255,0,10)
        self.nbVie = 3
        #self.posVie = Vector2(700,30)
        self.rayon = 40
        #self.score = 0

    def deplacement(self):

        if self.acc.length() > self.accMax:
            self.acc.scale_to_length(self.accMax)
        if self.vitesse.length() > self.vitesseMax:
            self.vitesse.scale_to_length(self.vitesseMax)

        if core.getKeyPressList("a"): #Tourner a gauche
            self.orientation = self.orientation.rotate(-5)

        if core.getKeyPressList("z"): #Tourner a droite
            self.orientation = self.orientation.rotate(5)

        if core.getKeyPressList("m"): #Avancer
            self.acc = Vector2(self.orientation)
            self.vitesse += self.acc
            self.pos += self.orientation

        self.pos += self.acc
        self.acc = self.acc * 0.99


    def comptage(self):
        pass

    def show(self):
        #core.memory("texture", core.Texture("./vaisseau.png", self.pos, 0, (60,60)))
        #if not core.memory("texture").ready:
         #   core.memory("texture").load()
          #  core.memory("texture").show()

        p1 =  self.orientation.rotate(90)
        p1.scale_to_length(15)
        p1+=self.pos
        p3 = self.orientation.rotate(-90)
        p3.scale_to_length(15)
        p3+=self.pos
        p2 = Vector2(self.orientation)
        p2.scale_to_length(35)#Sommet du triangle
        p2+=self.pos

        core.Draw.polygon(self.color,((p1), (p2), (p3)))

        #Crée un cercle dans un triangle
        hauteur = Vector2(self.orientation)
        hauteur.scale_to_length(35/3)
        hauteur += self.pos
        #core.Draw.circle((0,0,0), hauteur, self.rayon, 2)

        if self.pos.x<0: #Telporter a droite
            self.pos.x = 800

        if self.pos.x>800: #Teleporter a gauche
            self.pos.x = 0

        if self.pos.y<0: #Teleporter en bas
            self.pos.y = 500

        if self.pos.y>500: #Teleporter en haut
            self.pos.y = 0

    def showVie(self): #Affichage des vies:
        if self.nbVie == 3:
            core.memory("texture", core.Texture("./coeur_vie.png", (750,10), 0, (45,45)))
            if not core.memory("texture").ready:
                core.memory("texture").load()
                core.memory("texture").show()

            core.memory("texture", core.Texture("./coeur_vie.png", (710,10), 0, (45,45)))
            if not core.memory("texture").ready:
                core.memory("texture").load()
                core.memory("texture").show()

            core.memory("texture", core.Texture("./coeur_vie.png", (670,10), 0, (45,45)))
            if not core.memory("texture").ready:
                core.memory("texture").load()
                core.memory("texture").show()

        if self.nbVie == 2:
            core.memory("texture", core.Texture("./coeur_vie.png", (750, 10), 0, (45, 45)))
            if not core.memory("texture").ready:
                core.memory("texture").load()
                core.memory("texture").show()

            core.memory("texture", core.Texture("./coeur_vie.png", (710, 10), 0, (45, 45)))
            if not core.memory("texture").ready:
                core.memory("texture").load()
                core.memory("texture").show()

        if self.nbVie == 1:
            core.memory("texture", core.Texture("./coeur_vie.png", (750, 10), 0, (45, 45)))
            if not core.memory("texture").ready:
                core.memory("texture").load()
                core.memory("texture").show()

        core.Draw.rect((255,0,10), (670, 5, 125, 55), 2)





