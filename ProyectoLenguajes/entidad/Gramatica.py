
#Clase gramatica que contiene su gramatica y los terminales
#pertenecientes a este
#@version 1.0

class Gramatica:

    def _init_(self,gramatica,terminales):
        self.gramatica =gramatica
        self.terminales=terminales

#se lee el archivo de texto  con la gramatica para generar un diccionarion con toda esta informacion
#si el archivo no es .txt se lanza una excepcion

    def leerGramatica(self,archivo):
        print("")

#metodo que crea los terminales, este se genera por medio de un archivo de texto
#que al leerse se interpretara la informacion para poder crear los terminales
#son los valoes iniciales en los saltos de texto antes de una flecha
#@:param nombre del terminal que se agregara al diccionario terminales

    def crearTerminales(self,nombre):
        print("")

#  metodo que calcula los primeros dado el terminal
 # @:param nombre valor del terminal

    def calcularPrimeros(self,nombre):
        print("")

#metodo que calcula los segundos dado el terminal
#@param nombre del terminal

    def calcularSegundos(self,nombre):
        print("")

#se genera el automata con la informacion de la gramatica,
    def  llenarAutomata(self):
        print("")
