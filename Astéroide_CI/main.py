import random
import time
import sys

import pygame.image
from pygame import Vector2
from pygame.rect import Rect

import core
from Astéroide_CI.comete import Comete
from Astéroide_CI.partie import Partie
from Astéroide_CI.etat import Etat
from Astéroide_CI.projectile import Projectile


def creationComete(position_x,position_y, rayon, vitesseMax):
    aste = Comete() #Creation asteroide par defaut avec toute les valeurs du constructeur
    aste.position = Vector2(position_x,position_y)
    aste.acc = Vector2(random.uniform(-1,1), random.uniform(-1,1)) #On attribut une acceleration aleatoire
    aste.rayon = rayon
    aste.vitesseMax = vitesseMax
    core.memory("mesCometes").append(aste) #Je l'ajoute a la liste d'asteroides

def creationProjectile():
    proj = Projectile()
    proj.position = Vector2(core.memory("partie").joueur.pos) + 35*core.memory("partie").joueur.orientation
    proj.acc = Vector2(core.memory("partie").joueur.orientation)
    core.memory("mesProjectiles").append(proj)


def afficherMENU():
    core.memory("texture", core.Texture("./Planete.jpg", Vector2(0, 0), 0, [800, 500]))
    if not core.memory("texture").ready:
        core.memory("texture").load()
    core.memory("texture").show()

    core.Draw.text((255, 255, 255), "PLAY", (70, 225), 30, "Bauhaus 93")
    core.Draw.text((255, 255, 255), "ASTEROÏDE", (70, 150), 60, "Bauhaus 93")
    core.Draw.text((255, 255, 255), "A: ORIENTATION A DROITE", (560, 50), 25, "Calibri (Corps)")
    core.Draw.text((255, 255, 255), "Z: ORIENTATION A GAUCHE", (560, 70), 25, "Calibri (Corps)")
    core.Draw.text((255, 255, 255), "M: AVANCER", (560, 90), 25, "Calibri (Corps)")
    core.Draw.text((255, 255, 255), "SPACE: TIRER", (560, 110), 25, "Calibri (Corps)")
    core.Draw.text((255,255,255), "EXIT", (70,450), 30, "Bauhaus 93")

    #core.Draw.rect((250, 250, 250), (550, 390, 250, 100), 3)

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(70, 225, 80, 40)
        if rec.collidepoint(position):
            core.memory("etat", Etat.JEU)

    if core.getKeyPressList("RETURN"):
        core.memory("etat", Etat.JEU)

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(70, 450, 80, 80)
        if rec.collidepoint(position):
            sys.exit()

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(70, 225, 80, 40)
        if rec.collidepoint(position):
            core.Draw.text((255, 0, 0), "PLAY", (70, 225), 30, "Bauhaus 93")

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(70, 450, 80, 50)
        if rec.collidepoint(position):
            core.Draw.text((255, 255, 0), "EXIT", (70, 450), 30, "Bauhaus 93")

def afficherJEU():

    core.memory("partie").control()
    core.memory("partie").show()
    #core.Draw.rect((250, 250, 250), (0, 350, 40, 40))  # CP

    compteur = (core.memory("score"))
    core.Draw.text((255,255,255),"POINTS: ", (1,1), 25, "Arial")

    #if core.getMouseLeftClick():                        #CP
     #   position = core.getMouseLeftClick()             #CP
      #  rec = Rect(0,350,40,40)                         #CP
       # if rec.collidepoint(position):                  #CP
            #core.memory("etat", Etat.GAMEOVER)          #CP

    for c in core.memory("mesCometes"):
        c.draw()
        c.deplacement()


    #Création des projectiles
    if core.getKeyPressList("SPACE"):
        if len(core.memory("mesProjectiles"))>0: #Comparaison de la longueur de la liste vide ou pas
            if time.time() - core.memory("mesProjectiles")[-1].startTime>0.2: #Je verifie que le dernier projectile a ete lance il y a 0.2ms
                creationProjectile()
        else:
            creationProjectile() #Comme la liste est vide on cree dans tt les cas un projectile

    #Disparition des projectiles
    for p in core.memory("mesProjectiles"):
        if time.time() - p.startTime > p.dureeDeVie: #Le temps qu'il - le temps de creation superieur a la duree de vie
            core.memory("mesProjectiles").remove(p)

     #Afficher les projectiles
    for p in core.memory("mesProjectiles"):
        p.deplacement()
        p.draw()

    #Tester les collisions asteroides et projectiles
    for c in core.memory("mesCometes"):
        for p in core.memory("mesProjectiles"):
            res = c.collision_projectile(p)
            if res:
                if c.rayon >20:
                    creationComete(p.position.x, p.position.y, c.rayon/2, c.vitesseMax+2)
                    creationComete(p.position.x, p.position.y, c.rayon / 2, c.vitesseMax+2)
                    if c.rayon == 50:
                        compteur +=30
                    else:
                        compteur +=60
                else:
                    compteur += 120
                core.memory("mesProjectiles").remove(p)
                core.memory("mesCometes").remove(c)
                core.memory("score",compteur)

    if not core.memory("mesCometes"):
        for i in range(0, 6):  # création de seulement 5 comètes
            alea = random.randint(0, 3)  # Generation nombre aleatoire pr les zones de spawn
            if alea == 0:  # afficher les asteroides en haut
                position_x = random.randint(0, 800)
                position_y = -10
            if alea == 1:  # afficher les ateroides en Bas
                position_x = random.randint(0, 800)
                position_y = 510
            if alea == 2:  # afficher les asteroides a Gauche
                position_x = -10
                position_y = random.randint(0, 500)
            if alea == 3:  # afficher les asteroides a Droite
                position_x = 810
                position_y = random.randint(0, 500)
            creationComete(position_x, position_y, 50, 1)  # Creation asteroide avec les coordonnée x,y calculé avant
        print("liste vide")

    #Tester les collisions asteroides et vaisseau et perdre de la vie
    for c in core.memory("mesCometes"):
        res = c.collision_joueur(core.memory("partie").joueur)
        if res:
            core.memory("partie").joueur.nbVie -= 1 #On retire une vie des qu'on touche un asteroide

            if c.rayon > 20: #Division des asteroides
                creationComete(c.position.x, c.position.y, c.rayon / 2, c.vitesseMax+2)
                creationComete(c.position.x, c.position.y, c.rayon / 2, c.vitesseMax+2)
            core.memory("mesCometes").remove(c) #Disparition des asteroides
            core.memory("partie").joueur.pos = Vector2(400,250)#Remettre le joueur a sa place

            if core.memory("partie").joueur.nbVie == 0: #Si on a plus de vie alors game over
                core.memory("etat", Etat.GAMEOVER)


    core.Draw.text((255, 255, 255), str(core.memory("score")), (100, 1), 25, "Arial")


def afficherGAMEOVER():
    core.memory("texture", core.Texture("./Planete.jpg", Vector2(0, 0), 0, [800, 500]))
    if not core.memory("texture").ready:
        core.memory("texture").load()
        core.memory("texture").show()


    core.Draw.text((255, 255, 255), "GAME OVER", (250, 150), 50, "Bauhaus 93")  # CP
    core.Draw.text((255,255,255), "Votre score:", (250,230), 35, "Bauhaus 93")
    core.Draw.text((255, 255, 255), str(core.memory("score")), (470, 230), 35, "Bauhaus 93")
    core.Draw.text((255, 255, 255), "MENU", (200, 300), 50, "Bauhaus 93")  # CP
    core.Draw.text((255, 255, 255), "PLAY", (450, 300), 50, "Bauhaus 93")  # CP
    core.Draw.text((255,255,255), "EXIT", (70, 450), 30, "Bauhaus 93")
    #core.Draw.rect((250, 250, 250), (270, 300, 40, 40))   #CP

    if core.getMouseLeftClick():  # CP
        position = core.getMouseLeftClick()  # CP
        rec = Rect(200, 300, 125, 50)  # CP
        if rec.collidepoint(position):  # CP
            core.memory("partie").joueur.nbVie = 3
            core.memory("partie").joueur.pos = Vector2(400, 250)  # Remettre le joueur a sa place
            core.memory("partie").joueur.orientation = Vector2(0, -1)  # Remettre le joueur a sla bonne orientation
            core.memory("partie").joueur.vitesse = Vector2(0, 0)
            core.memory("partie").joueur.acc = Vector2(0, 0)

            for c in core.memory("mesCometes"):
                core.memory("mesCometes").clear()

            for i in range(0, 6):  # création de seulement 5 comètes
                alea = random.randint(0, 3)  # Generation nombre aleatoire pr les zones de spawn
                if alea == 0:  # afficher les asteroides en haut
                    position_x = random.randint(0, 800)
                    position_y = -10
                if alea == 1:  # afficher les ateroides en Bas
                    position_x = random.randint(0, 800)
                    position_y = 510
                if alea == 2:  # afficher les asteroides a Gauche
                    position_x = -10
                    position_y = random.randint(0, 500)
                if alea == 3:  # afficher les asteroides a Droite
                    position_x = 810
                    position_y = random.randint(0, 500)
                creationComete(position_x, position_y, 50,
                               1)  # Creation asteroide avec les coordonnée x,y calculé avant

            compteur = 0
            core.memory("score", compteur)
            core.memory("etat", Etat.MENU)  # CP

    if core.getMouseLeftClick():  # CP
        position = core.getMouseLeftClick()  # CP
        rec = Rect(450, 300, 115, 50)  # CP
        if rec.collidepoint(position):  # CP
            core.memory("partie").joueur.nbVie = 3
            core.memory("partie").joueur.pos = Vector2(400, 250)  # Remettre le joueur a sa place
            core.memory("partie").joueur.orientation = Vector2(0, -1)  # Remettre le joueur a sla bonne orientation
            core.memory("partie").joueur.vitesse = Vector2(0,0)
            core.memory("partie").joueur.acc = Vector2(0, 0)

            for c in core.memory("mesCometes"):
                core.memory("mesCometes").clear()


            for i in range(0, 6):  # création de seulement 5 comètes
                alea = random.randint(0, 3)  # Generation nombre aleatoire pr les zones de spawn
                if alea == 0:  # afficher les asteroides en haut
                    position_x = random.randint(0, 800)
                    position_y = -10
                if alea == 1:  # afficher les ateroides en Bas
                    position_x = random.randint(0, 800)
                    position_y = 510
                if alea == 2:  # afficher les asteroides a Gauche
                    position_x = -10
                    position_y = random.randint(0, 500)
                if alea == 3:  # afficher les asteroides a Droite
                    position_x = 810
                    position_y = random.randint(0, 500)
                creationComete(position_x, position_y, 50,1)  # Creation asteroide avec les coordonnée x,y calculé avant

            compteur = 0
            core.memory("score", compteur)
            core.memory("etat", Etat.JEU)  # CP

    if core.getKeyPressList("RETURN"):
        core.memory("etat", Etat.JEU)

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(200, 300, 125, 50)
        if rec.collidepoint(position):
            core.Draw.text((255, 0, 0), "MENU", (200, 300), 50, "Bauhaus 93")

    if core.getMouseLeftClick():
        position = core.getMouseLeftClick()
        rec = Rect(70, 450, 80, 80)
        if rec.collidepoint(position):
            sys.exit()

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(450, 300, 115, 50)
        if rec.collidepoint(position):
            core.Draw.text((255, 0, 0), "PLAY", (450, 300), 50, "Bauhaus 93")

    if core.getMouseLocation():
        position = core.getMouseLocation()
        rec = Rect(70, 450, 80, 50)
        if rec.collidepoint(position):
            core.Draw.text((255, 255, 0), "EXIT", (70, 450), 30, "Bauhaus 93")

def setup():
    print("Start setup")
    core.WINDOW_SIZE = [800, 500]
    core.fps = 30

    core.memory("etat", Etat.MENU)

    core.memory("PacificCoastHighway", core.Sound("PacificCoastHighway.mp3"))

    core.memory("partie", Partie())

    core.memory("mesCometes", [])  # Creation d'une liste de taille inconnue

    core.memory("mesProjectiles", [])
    core.memory ("score",0)

    for i in range(0,6): #création de seulement 5 comètes
        alea = random.randint(0, 3) #Generation nombre aleatoire pr les zones de spawn
        if alea == 0:  # afficher les asteroides en haut
            position_x = random.randint(0, 800)
            position_y = -10
        if alea == 1:  # afficher les ateroides en Bas
            position_x = random.randint(0, 800)
            position_y = 510
        if alea == 2:  # afficher les asteroides a Gauche
            position_x = -10
            position_y = random.randint(0, 500)
        if alea == 3:  # afficher les asteroides a Droite
            position_x = 810
            position_y = random.randint(0, 500)
        creationComete(position_x, position_y, 50, 1) #Creation asteroide avec les coordonnée x,y calculé avant
    print("End setup")


def run():
    core.cleanScreen()

    core.memory("PacificCoastHighway").start()

    if core.getKeyPressList("r"):
        core.memory("PacificCoastHighway").rewind()

    if core.getKeyPressList("p"):
        core.memory("PacificCoastHighway").pause()

    if core.memory("etat") == Etat.MENU:
        afficherMENU()

    if core.memory("etat") == Etat.JEU:
        afficherJEU()

    if core.memory("etat") == Etat.GAMEOVER:
        afficherGAMEOVER()

def getMouseLocation():
    return pygame.mouse.get_pos()

core.main(setup, run)
