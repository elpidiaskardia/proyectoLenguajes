
#Clase gramatica que contiene su gramatica y los terminales
#pertenecientes a este
#@version 2.0
from graphviz import *
import os
from entidad.NoTerminal import NoTerminal
from entidad.Nodo import Nodo
from entidad.Automata import Automata

class Gramatica:
    automata = Automata()
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
        prueba_punto =self.ponerPuntosGramatica(self.gramaticaa)
        for llave,val in prueba_punto.items():
            print('no terminal->> '+llave)
            for expresion in val.expresiones:
<<<<<<< HEAD
                print('expresion con punto='+expresion)
=======
                print('estos papi== '+expresion)
        self.pruebaImp()

>>>>>>> fa682f476cb73773b7cd0ceab16b2a5890512f6b

#  metodo que calcula los primeros dado el terminal
    def pruebaImp(self):
        g = Graph(format='dot')
        for llaver,valor in self.gramaticaa.items():

            Nodo = llaver +'\n Primeros=  '
            for primero in valor.primeros:
                Nodo += primero + '  '
            Nodo +='  \n siguiente=  '
            for siguiente in valor.siguientes:
                Nodo += siguiente + '  '
            Nodo += ' '
            g.edge(Nodo, 'ALV si dio, Traiga ronnnn')


        g.save()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/'
        os.system('dot -Tpng Graph.gv -o random.png')

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
                    self.gramaticaa.get(noteminal).agregarPrimeros(self.gramaticaa.get(Expresion[0]).primeros)



           #     if  Expresion[0] =='λ':
            #        self.gramaticaa.get(nombre).keys()[0].primeros.append(auxiliarExpresion)
#metodo que calcula los segundos dado el terminal
#@param nombre del terminal

    def calcularSiguientes(self):
        self.gramaticaa.get('S`').agregarSiguiente('$')
        for noterminal1 in self.gramaticaa.keys():
            for noteminal in self.gramaticaa.keys():
                    #los no terminales y sacar sus siguientes
                    for Expresion in self.gramaticaa.get(noteminal).expresiones:
                        listaExpresion =  Expresion.split(' ')
                        for auxExpresion in listaExpresion:
                            if noterminal1 ==  auxExpresion.strip():
                                siguientee =  listaExpresion.index(auxExpresion)+1
                                if siguientee  < len(listaExpresion):
                                    if listaExpresion[siguientee].strip() not in self.gramaticaa.keys():
                                        self.gramaticaa.get(noterminal1).agregarSiguiente(listaExpresion[siguientee].strip())
                                    else :#aqui van los siguientes que son no terminales
                                        self.gramaticaa.get(noterminal1).agregarSiguientes(self.gramaticaa.get(listaExpresion[siguientee].strip()).primeros)



        for noterminal1 in self.gramaticaa.keys():
            for noteminal in self.gramaticaa.keys():
                # los no terminales y con siguiente vacio
                for Expresion in self.gramaticaa.get(noteminal).expresiones:
                    listaExpresion = Expresion.split(' ')
                    for auxExpresion in listaExpresion:
                        if noterminal1 == auxExpresion.strip():
                            siguientee = listaExpresion.index(auxExpresion) + 1
                            if siguientee  == len(listaExpresion):
                                self.gramaticaa.get(noterminal1).agregarSiguientes(self.gramaticaa.get(noteminal).siguientes)

    def imprimirSiguientes(self):
        for llaver,valor in self.gramaticaa.items():
            print('No terminal: '+ llaver)
            for siguientes in valor.siguientes:
                print('siguientes: '+ siguientes)
            for expreciones in valor.expresiones:
                 print('expresion: ' + expreciones)
    #Agrega los puntos iniciales a las expresiones de los no terminales
    def ponerPuntosGramatica(self,gramatica):
        for noterminal in gramatica.keys():
            for expresion in gramatica.get(noterminal).expresiones:
                    ubicacion = gramatica.get(noterminal).expresiones.index(expresion)
                    gramatica.get(noterminal).expresiones[ubicacion] = ('.' + expresion)


        return gramatica

    #se genera el automata con la informacion de la gramatica,

    def  llenarAutomataLR0(self,gramatica):
        gramatica=self.OrganizarLR0PuntosSiguientes(gramatica)


    def OrganizarLR0PuntosSiguientes(self,gramatica):
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if  auxExpresion.strip()=='.':
                        punto = auxExpresion.index('.')
                    # NOterminal
                        if punto + 1 <len(listaExpresion)and listaExpresion[punto + 1].strip() in gramatica.keys():
                            gramatica[listaExpresion[punto + 1]] = self.gramaticaa.get(listaExpresion[punto + 1])
                            # siguen los llamados recursivos y listo papus ;v
        return gramatica