
#Clase gramatica que contiene su gramatica y los terminales
#pertenecientes a este
#@version 2.0
from entidad.NoTerminal import NoTerminal


class Gramatica:

    gramaticaa={}
    noterminal=[]
    def __init__(self):
        self.gramaticaa={'S`':NoTerminal('S`')}
        self.noterminal=[]

#se lee el archivo de texto  con la gramatica para generar un diccionarion con toda esta informacion
#si el archivo no es .txt se lanza una excepcion

    def leerGramatica(self,archivo):
        f = open(archivo,"r")

        for linea in f.readlines():
          expresion = linea.split('->')
          if    expresion[0] in list(self.gramaticaa):
              self.gramaticaa.get(expresion[0]).expresiones.append(  expresion[1])
          else:
              self.gramaticaa[ expresion[0] ] =  NoTerminal( expresion[0])
              self.gramaticaa.get(expresion[0]).expresiones.append(  expresion[1])
        f.close()
        self.gramaticaa.get('S`').expresiones.append(list(self.gramaticaa)[1])

        self.calcularPrimeros( )
        self.imprimirPrimero()
        self.calcularSiguientes()
        self. imprimirSiguientes()

#  metodo que calcula los primeros dado el terminal

    def imprimirPrimero(self):
        for llaver,valor in self.gramaticaa.items():
            print('No terminal: '+ llaver)
            for primero in valor.primeros:
                print('primerps: '+ primero)
            for expreciones in valor.expresiones:
                 print('espresion: ' + expreciones)

    def calcularPrimeros(self):

        for noteminal in self.gramaticaa.keys():
            for Expresion in self.gramaticaa.get(noteminal).expresiones:
                auxExpresion = Expresion.split(' ')
                if auxExpresion[0].strip() not in self.gramaticaa.keys():
                     self.gramaticaa.get(noteminal).agregarPrimero(auxExpresion[0].strip())

        for noteminal in reversed(list(self.gramaticaa)):
            for Expresion in self.gramaticaa.get(noteminal).expresiones:
                if Expresion[0]  in self.gramaticaa.keys():
                    self.gramaticaa.get(noteminal).primeros += self.gramaticaa.get(Expresion[0]).primeros



           #     if  Expresion[0] =='λ':
            #        self.gramaticaa.get(nombre).keys()[0].primeros.append(auxiliarExpresion)
#metodo que calcula los segundos dado el terminal
#@param nombre del terminal

    def calcularSiguientes(self):

        for noteminal in self.gramaticaa.keys():
            if noteminal =='S`':
                self.gramaticaa.get('S`').siguientes.append('$')
            else :
                #no se recorre toda la gramatica, es necesario cambiar eso para poder mirar en donde estan
                #los no terminales y sacar sus siguientes
                for Expresion in self.gramaticaa.get(noteminal).expresiones:
                    auxExpresion = Expresion.split(' ')
                    if noteminal in  auxExpresion:
                        siguientee =  auxExpresion.index(noteminal)+1
                        if  auxExpresion[siguientee] not in self.gramaticaa.keys():
                            self.gramaticaa.get(noteminal).siguientes.append( auxExpresion[siguientee])
                        else :
                            print('aqui van los siguientes que son no terminales')

    def imprimirSiguientes(self):
        for llaver,valor in self.gramaticaa.items():
            print('No terminal: '+ llaver)
            for siguientes in valor.siguientes:
                print('siguientes: '+ siguientes)
            for expreciones in valor.expresiones:
                 print('expresion: ' + expreciones)
    #se genera el automata con la informacion de la gramatica,
    def  llenarAutomata(self):
        print("")

