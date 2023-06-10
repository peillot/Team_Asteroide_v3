import random
import time

from pygame import Vector2

import core
from Astéroide_CI.comete import Comete
from Astéroide_CI.player import Player
from Astéroide_CI.projectile import Projectile


class Map:
    def __init__(self):
        self.taille = Vector2(core.WINDOW_SIZE)


    def show(self,map):

        if map ==1:
            core.memory("texture", core.Texture("./Galaxie.jpg", Vector2(0, 0), 0, [800, 500]))
            if not core.memory("texture").ready:
                core.memory("texture").load()
            core.memory("texture").show()
        if map == 2:
            core.memory("texture", core.Texture("./Galaxie_noir.png", Vector2(0, 0), 0, [800, 500]))
            if not core.memory("texture").ready:
                core.memory("texture").load()
            core.memory("texture").show()
        #core.Draw.rect((255, 0, 0), (0,510, 800, 5))  # Zone Spawn en bas
        #core.Draw.rect((255, 0, 0), (0,-10, 800, 5))  # Zone Spawn en haut
        #core.Draw.rect((255, 0, 0), (-10,0, 5, 500))  # Zone Spawn a gauche
        #core.Draw.rect((255, 0, 0), (810,0, 5, 500))  # Zone Spawn a droite

        #core.Draw.rect((0, 255, 0), (0, 520, 800, 40))  # Zone Teleportation en bas
        #core.Draw.rect((0, 255, 0), (0, -50, 800, 40))  # Zone Teleportation en haut
        #core.Draw.rect((0, 255, 0), (-50, 0, 40, 500))  # Zone Teleportation a gauche
        #core.Draw.rect((0, 255, 0), (820, 0, 40, 500))  # Zone Teleportation a droite



