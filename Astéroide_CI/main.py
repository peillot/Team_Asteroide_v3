import time

import pygame.image
from pygame import Vector2
from pygame.rect import Rect

import core
from Astéroide_CI import etat
from Astéroide_CI.Partie import Partie
from Astéroide_CI.Partie import Player
from Astéroide_CI.etat import Etat



def afficherMENU():
    #core.Draw.rect((0 ,0 , 0), (250, 230, 90, 40))
    core.memory("texture", core.Texture("./Planete.jpg", Vector2(0, 0), 0, [800, 500]))
    if not core.memory("texture").ready:
        core.memory("texture").load()
    core.memory("texture").show()

    core.Draw.text((255, 255, 255), "PLAY",(70, 225), 30, "Bauhaus 93")
    core.Draw.text((255, 255, 255), "ASTEROÏDE", (70, 150), 60, "Bauhaus 93")
    core.Draw.text((255, 255, 255), "A: ORIENTATION A DROITE",(560, 400), 25, "Calibri (Corps)")
    core.Draw.text((255, 255, 255), "Z: ORIENTATION A GAUCHE", (560, 420), 25, "Calibri (Corps)")
    core.Draw.text((255, 255, 255), "M: AVANCER", (560, 440), 25, "Calibri (Corps)")
    core.Draw.text((255, 255, 255), "SPACE: TIRER", (560, 460), 25, "Calibri (Corps)")

    core.Draw.rect((250 ,250 , 250), (550, 390, 250, 100),3)


    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(70, 225, 80, 40)
        if rec.collidepoint(position):
            core.memory("etat", Etat.JEU)

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(70, 225, 80, 40)
        if rec.collidepoint(position):
            core.Draw.text((255, 0, 0), "PLAY", (70, 225), 30, "Bauhaus 93")

def afficherJEU():

    core.memory("texture", core.Texture("./Galaxie.jpg", Vector2(0, 0), 0, [800, 500]))
    if not core.memory("texture").ready:
        core.memory("texture").load()
    core.memory("texture").show()

    core.Draw.rect((250, 250, 250), (0, 350, 40, 40))   #CP
    core.memory("partie", Partie())
    #core.memory("partie").show()
    core.memory("partie").control()


    if core.getMouseLeftClick():                        #CP
        position = core.getMouseLeftClick()             #CP
        rec = Rect(0,350,40,40)                         #CP
        if rec.collidepoint(position):                  #CP
            core.memory("etat", Etat.GAMEOVER)          #CP





def afficherGAMEOVER():


    core.memory("texture", core.Texture("./Planete.jpg", Vector2(0, 0), 0, [800, 500]))
    if not core.memory("texture").ready:
        core.memory("texture").load()
        core.memory("texture").show()


    core.Draw.text((255, 255, 255), "GAME OVER", (250, 200), 50, "Bauhaus 93")  # CP
    core.Draw.text((255, 255, 255), "MENU", (200, 300), 50, "Bauhaus 93")  # CP
    core.Draw.text((255, 255, 255), "PLAY", (450, 300), 50, "Bauhaus 93")  # CP
    #core.Draw.rect((250, 250, 250), (270, 300, 40, 40))   #CP

    if core.getMouseLeftClick():  # CP
        position = core.getMouseLeftClick()  # CP
        rec = Rect(200, 300, 50, 50)  # CP
        if rec.collidepoint(position):  # CP
            core.memory("etat", Etat.MENU)  # CP

    if core.getMouseLeftClick():  # CP
        position = core.getMouseLeftClick()  # CP
        rec = Rect(450, 300, 50, 50)  # CP
        if rec.collidepoint(position):  # CP
            core.memory("etat", Etat.JEU)  # CP

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(200, 300, 100, 50)
        if rec.collidepoint(position):
            core.Draw.text((255, 0, 0), "MENU", (200, 300), 50, "Bauhaus 93")

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(450, 300, 100, 50)
        if rec.collidepoint(position):
            core.Draw.text((255, 0, 0), "PLAY", (450, 300), 50, "Bauhaus 93")




def setup():
    print("Start setup")
    core.WINDOW_SIZE = [800, 500]
    core.fps = 60
    core.memory("etat", Etat.MENU)
    print("End setup")


def run():
    core.cleanScreen()



    if core.memory("etat") == Etat.MENU:
        afficherMENU()

    if core.memory("etat") == Etat.JEU:
        afficherJEU()

    if core.memory("etat") == Etat.GAMEOVER:
        afficherGAMEOVER()


def getMouseLocation():
    return pygame.mouse.get_pos()


core.main(setup, run)
