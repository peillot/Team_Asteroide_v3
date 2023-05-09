import random
import time
from pygame import Vector2
import core
from projectile.projectiles import Projectile


def setup():
    core.WINDOW_SIZE = [800,800]
    core.fps = 30

    core.memory("mesProjectiles", []) #Creation d'une liste de taille inconnue


def creationProjectile(position):
    proj = Projectile() #Creation projectile par defaut avec toute les valeurs du constructeur
    proj.position = Vector2(position) #On attribut la position du clic souris
    proj.acc = Vector2(random.uniform(-1,1), random.uniform(-1,1)) #On attribut une acceleration aleatoire
    core.memory("mesProjectiles").append(proj) #Je l'ajoute a la liste de projectile


def run():
    core.cleanScreen() #Nettoyer l'ecran de la frame précedente

    #Création des projectiles lors d'un clic souris toutes les 0.2ms
    if core.getMouseLeftClick():
        if len(core.memory("mesProjectiles"))>0: #Comparaison de la longueur de la liste vide ou pas
            if time.time() - core.memory("mesProjectiles")[-1].startTime>0.2: #Je verifie que le dernier projectile a ete lance il y a 0.2ms
                creationProjectile(core.getMouseLeftClick())

        else:
            creationProjectile(core.getMouseLeftClick()) #Comme la liste est vide on cree dans tt les cas un projectile

    #Disparition des projectiles
    for p in core.memory("mesProjectiles"):
        if time.time() - p.startTime > p.dureeDeVie: #Le temps qu'il - le temps de creation superieur a la duree de vie
            core.memory("mesProjectiles").remove(p)


     #Afficher les projectiles
    for p in core.memory("mesProjectiles"):
        p.deplacement()
        p.draw()


core.main(setup,run) #Lancer le programme