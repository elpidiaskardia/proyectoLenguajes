from tkinter import *
import pygame
#clase que se encarga de general el automata y la tabla
#version 1.0

class Animacion:

    def __init__(self):

        pygame.init()
        pygame.display.get_init()
        # mostrar ventana con dimenciones x y
        size = 900, 650
        self.screen = pygame.display.set_mode(size)
        # cambio titulo
        pygame.display.set_caption('Animacion')
        self.colorA = 255, 247, 236



        pygame.display.update()

    def generarAutomataLr0(self):
        imagen = pygame.image.load('Lr0.png')
        imagen = pygame.transform.scale(imagen,(900, 650))
        self.screen.blit(imagen, (0, 0))
        pygame.display.update()

    # metodo que genera el automata de la gramatica lr1
    def generarAutomataLr1(self):
        imagen = pygame.image.load('Lr1.png')
        imagen = pygame.transform.scale(imagen,(900, 650))
        self.screen.blit(imagen, (0, 0))
        pygame.display.update()



