from pygame.rect import Rect

import core
from Astéroide_CI import etat
from Astéroide_CI.Partie import Partie
from Astéroide_CI.Partie import Player
from Astéroide_CI.etat import Etat


def afficherMENU():
    core.Draw.rect((0 ,100 , 255), (250, 230, 90, 40))
    core.Draw.text((255, 255, 255), "PLAY",(260, 230), 30, "Arial")
    core.Draw.text((255, 255, 255), "ASTEROÏDE", (120, 15), 60, "CASTELLAR")

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(250, 230, 80, 40)
        if rec.collidepoint(position):
            core.memory("etat", Etat.JEU)


def afficherJEU():
    core.memory("partie", Partie())
    core.memory("partie").show()
    core.memory("partie").control()



def afficherGAMEOVER():
    print("GAMEOVER")


def setup():
    print("Start setup")
    core.WINDOW_SIZE = [600, 400]
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


core.main(setup, run)
