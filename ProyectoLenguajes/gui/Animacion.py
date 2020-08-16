from tkinter import *
import pygame
#clase que se encarga de general el automata y la tabla
#version 1.0
class Animacion:

    def __init__(self,ControlGramatica):
        self.ControlGramatica=ControlGramatica

        pygame.init()
        pygame.display.get_init()
        # mostrar ventana con dimenciones x y
        size = 900, 650
        self.screen = pygame.display.set_mode(size)
        # cambio titulo
        pygame.display.set_caption('Animacion')
        self.colorA = 255, 247, 236

