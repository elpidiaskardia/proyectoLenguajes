
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
    gramaticaaPuntos={}
    gramaticaPuntosComas={}
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

        #self.calcularPrimeros( )
        #self.imprimirPrimero()
        #self.calcularSiguientes()
        #self. imprimirSiguientes()
        #self.gramaticaaPuntos =self.gramaticaa
        #self.gramaticaaPuntos= self.ponerPuntosGramatica(self.gramaticaaPuntos)
        #self.pruebaImp()
        self.gramaticaPuntosComas =self.gramaticaa
        self.gramaticaPuntosComas =self.ponerPuntosYComasGramaticaLr0(self.gramaticaPuntosComas)
        gramaticota = self.gramaticaPuntosComas
        prueba =self.ponerPrimerosLr1EnGramatica(gramaticota)
        for key, value in prueba.items():
            print('no terminal :'+key)
            for exp in value.expresiones:
                print('expresiones con primeros bien melas'+exp)



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
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin'
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
                    gramatica.get(noterminal).expresiones[ubicacion] = ('. ' + expresion)


        return gramatica

    #se genera el automata con la informacion de la gramatica,

    def  llenarAutomataLR0(self,gramatica):

        gramat=self.OrganizarLR0PuntosSiguientes(gramatica)
        nodito = Nodo(gramat)
        if self.verificarFinLro(gramat) ==True:

            self.automata.nodos.append(nodito)
        else:
            self.recursionLr0(gramat)

        return nodito

    def recursionLr0(self,gramatica):
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if auxExpresion.strip() == '.':
                        punto = auxExpresion.index('.')
                        if punto < len(listaExpresion):
                            siguiente = listaExpresion[punto+1].strip()
                            self.moviendoFilas(gramatica,siguiente)

    def moviendoFilas(self,gramatica,siguiente):
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                cumple=False
                for auxExpresion in listaExpresion:
                    if auxExpresion.strip() == '.':
                        punto = auxExpresion.index('.')
                        if punto < len(listaExpresion) and listaExpresion[punto +1].strip() ==siguiente:
                            cumple=True
                            ubicacionExpresion = gramatica.get(noterminal).expresiones.index(Expresion)
                            gramatica.get(noterminal).expresiones[ubicacionExpresion].replace('. ' + siguiente,siguiente + ' .')
                if cumple:
                    gramatica.get(noterminal).expresiones.pop(Expresion)
        self.llenarAutomataLR0(gramatica)

    def OrganizarLR0PuntosSiguientes(self,gramatica):
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if  auxExpresion.strip()=='.':
                        punto = auxExpresion.index('.')
                    # NOterminal
                        if punto + 1 <len(listaExpresion)and listaExpresion[punto + 1].strip() in gramatica.keys():
                            gramatica[listaExpresion[punto + 1]] = self.gramaticaaPuntos.get(listaExpresion[punto + 1])
                            # siguen los llamados recursivos y listo papus ;v
        return gramatica



    def verificarFinLro(self,gramatica):
        esFinal=True
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                if listaExpresion[len(listaExpresion)].strip()=='.' and esFinal:
                    esFinal=True
                else:
                    esFinal=False

        return esFinal

    #metodo que verifica si la gramatica lr1 es de acptacion en una expresion
    def verificarFinLr1(self,gramatica):
        esFinal = True
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for expresion in listaExpresion:
                    if expresion.strip()== '.':
                        siguientee = listaExpresion.index(expresion) + 1

                        if listaExpresion[siguientee].strip() == ',' and esFinal:
                            esFinal = True
                        else:
                            esFinal = False

        return esFinal

    def ponerPuntosYComasGramaticaLr0(self,gramatica):
        for noterminal in gramatica.keys():
            for expresion in gramatica.get(noterminal).expresiones:
                    ubicacion = gramatica.get(noterminal).expresiones.index(expresion)
                    gramatica.get(noterminal).expresiones[ubicacion] = '. ' + expresion + ' ,'


        return gramatica


    def ponerPrimerosLr1EnGramatica(self,gramatica):
        for noterminal in gramatica.keys():
            for expresion in gramatica.get(noterminal).expresiones:
                if noterminal =='S`':
                    ubicacion = gramatica.get(noterminal).expresiones.index(expresion)
                    gramatica.get(noterminal).expresiones[ubicacion] =  expresion + ' $'

                else:
                    listaExpresion = expresion.split(' ')
                    for auxExpresion in listaExpresion:
                        if auxExpresion.strip() == '.':
                            punto = auxExpresion.index('.')
                            print('holi we'+str(punto))
                            if punto + 2 < len(auxExpresion) and self.verificarFinLr1(gramatica)==False:
                                if auxExpresion[punto+2] not in gramatica.get(noterminal):
                                    ubicacion = gramatica.get(noterminal).expresiones.index(expresion)
                                    gramatica.get(noterminal).expresiones[ubicacion] = expresion + auxExpresion[punto+2]



        return gramatica