import core


class Comete:

    def __init__(self):
        self.taille1 = 30
        self.taille2 = 20
        self.taille3 = 10
        self.vitesseMax = 10
        self.accMax = 5

    def collide(self):
        pass

    def deplacement(self):
        pass

    def draw(self):
        core.Draw.circle((88,41,0), (100,100), self.taille1)
