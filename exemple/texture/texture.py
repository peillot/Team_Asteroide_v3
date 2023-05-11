import random
import time

from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [200, 200]
    core.memory("texture",core.Texture("./IMG_1774.png",Vector2(50,50)))

    print("Setup END-----------")


def run():
    core.cleanScreen()
    if not core.memory("texture").ready:
        core.memory("texture").load()


    #if core.getKeyPressList("b"):
        #core.memory("texture").box = not core.memory("texture").box
        #time.sleep(0.1)
        core.memory("texture").angle+=90
    core.memory("texture").show()

core.main(setup, run)
