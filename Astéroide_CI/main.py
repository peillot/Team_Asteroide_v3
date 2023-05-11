import random

import pygame.image
from pygame import Vector2
from pygame.rect import Rect

import core
from Astéroide_CI import etat
from Astéroide_CI.comete import Comete
from Astéroide_CI.partie import Partie
from Astéroide_CI.partie import Player
from Astéroide_CI.etat import Etat

def creationComete(position):
    aste = Comete() #Creation asteroide par defaut avec toute les valeurs du constructeur
    aste.position = Vector2(position)
    aste.acc = Vector2(random.uniform(-0.5,0), random.uniform(-0.5,0)) #On attribut une acceleration aleatoire
    core.memory("mesCometes").append(aste) #Je l'ajoute a la liste d'asteroides

def afficherMENU():
    core.Draw.rect((0 ,100 , 255), (355, 300, 90, 40))
    core.Draw.text((255, 255, 255), "PLAY",(370, 300), 30, "Arial")
    core.Draw.text((255, 255, 255), "ASTEROÏDE", (230, 25), 60, "CASTELLAR")

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(370, 300, 80, 40)
        if rec.collidepoint(position):
            core.memory("etat", Etat.JEU)


def afficherJEU():

    for c in core.memory("mesCometes"):
        c.draw()
        c.deplacement()

    core.memory("partie").control()
    core.memory("partie").show()




def afficherGAMEOVER():
    print("GAMEOVER")


def setup():
    print("Start setup")
    core.WINDOW_SIZE = [900, 600]
    core.fps = 30

    core.memory("etat", Etat.MENU)

    core.memory("partie", Partie())

    core.memory("mesCometes", [])  # Creation d'une liste de taille inconnue

    for i in range(0,5): #création de seulement 5 comètes
        creationComete(random.randint(100, 500)) #position aléatoire
    print("End setup")


def run():
    core.cleanScreen()

    if core.memory("etat") == Etat.MENU:
        afficherMENU()

    if core.memory("etat") == Etat.JEU:
        afficherJEU()

    if core.memory("etat") == Etat.GAMEOVER:
        afficherGAMEOVER()


core.main(setup, run)
