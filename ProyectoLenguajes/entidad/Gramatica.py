
#Clase gramatica que contiene su gramatica y los terminales
#pertenecientes a este
#@version 2.0
import os
from entidad.NoTerminal import NoTerminal
class Gramatica:
    gramaticaa={}
    noterminal=[]
    def _init_(self):
        self.gramaticaa ={}
        self.noterminal=[]

#se lee el archivo de texto  con la gramatica para generar un diccionarion con toda esta informacion
#si el archivo no es .txt se lanza una excepcion

    def leerGramatica(self,archivo):
        f = open(archivo,"r")
        for linea in f.readlines():
          expresion = linea.split('->')
          self.gramaticaa[expresion[0]] = {NoTerminal(expresion[0]): expresion[1]}
        f.close()

#  metodo que calcula los primeros dado el terminal


    def calcularPrimeros(self,nombre):
        auxiliarExpresion= self.gramaticaa.get(nombre).values()[0][0]
        if auxiliarExpresion in self.gramaticaa.keys():
            if self.gramaticaa.get(auxiliarExpresion).keys()[0].primeros == []:
                self.calcularPrimeros(auxiliarExpresion)
            else:
                self.gramaticaa.get(nombre).keys()[0].primeros += self.gramaticaa.get(auxiliarExpresion).keys()[0].primeros
        else:
            self.gramaticaa.get(nombre).keys()[0].primeros.append(auxiliarExpresion)

            if  auxiliarExpresion =="λ":
                self.gramaticaa.get(nombre).keys()[0].primeros.append(auxiliarExpresion)
#metodo que calcula los segundos dado el terminal
#@param nombre del terminal

    def calcularSiguientes(self,nombre):
        print("")

#se genera el automata con la informacion de la gramatica,
    def  llenarAutomata(self):
        print("")
