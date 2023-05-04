import core
from agario.Partie import Partie


def addBot():
    pass


def setup():
    print("Start setup")
    core.WINDOW_SIZE = [800, 600]
    core.fps = 80

    core.memory("Partie", Partie())
    core.memory("Partie").addPlayer()
    core.memory("Partie").addBots()


def run():
    core.cleanScreen()
    core.memory("Partie").show()


core.main(setup, run)
