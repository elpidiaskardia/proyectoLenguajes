
#Clase gramatica que contiene su gramatica y los terminales
#pertenecientes a este
#@version 2.0
from graphviz import *
import os
from ..entidad.NoTerminal import NoTerminal
from ..entidad.Nodo import Nodo
from ..entidad.Lr0 import Lr0
from ..entidad.Lr1 import Lr1

from ..entidad.Automata import Automata
from copy import *

class Gramatica:
    automata = Automata()
    gramaticaa={}
    gramaticaaPuntos={}
    gramaticaaComasPuntos={}
    noterminal=[]
    listnodoLr1=[]

    lr0=Lr0(gramaticaa)
    #Lr1=Lr0(gramaticaa)
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
        self.gramaticaa.get('S`').primeros.append('$')
        self.gramaticaa.get('S`').agregarExpresionPrimeroLr1('$')


        self.calcularPrimeros( )
        #self.imprimirPrimero()
        self.calcularSiguientes()
        #self. imprimirSiguientes()
        self.gramaticaaPuntos= self.ponerPuntosGramatica(deepcopy(self.gramaticaa))
        self.lr0.gramatica=deepcopy(self.gramaticaaPuntos)
        self.lr0.Crea()
        self.pruebaLR0(deepcopy(self.lr0.Principanodo))
        #self.ponerPuntosYComasGramaticaLr0(self.gramaticaPuntosComas)
        self.gramaticaaComasPuntos= deepcopy(self.gramaticaa)

        self.pruebaLR1(self.llenarAutomataLR1(deepcopy(self.prueba(self.ponerPuntosYComasGramaticaLr1(self.gramaticaaComasPuntos)))))
        #self.gramaticaPuntosComas = self.ponerPuntosYComasGramaticaLr0(self.gramaticaPuntosComas)
        #gramaticota = self.gramaticaPuntosComas
        #prueba = self.ponerPrimerosLr1EnGramatica(gramaticota)
        #for key, value in prueba.items():
        #  print('no terminal :' + key)
        #  for exp in value.expresiones:
        #     print('expresiones con primeros bien melas' + exp)


    def prueba (self,gramatica):
        gramatica2={}
        gramatica2=deepcopy(gramatica)
        for llaver in gramatica.keys():
            if  llaver != 'S`':
                gramatica2.pop(llaver)
        return deepcopy(gramatica2)





    def pruebaLR0(self,nodo):
        g = Graph(name='Lr0', format='dot')
        for llaver, valor in nodo.siguientes.items():
            if  valor  is not None:
                g.node(nodo.texto, shape='box',style='filled', fillcolor='darkolivegreen1')
                g.node(valor.texto, shape='box', style='filled', fillcolor='darkolivegreen1')
                if valor.siguientes=={}:
                    g.node(valor.texto, shape='box', style='filled', fillcolor='cyan4')

                else:
                    g.node(valor.texto,shape='box',style='filled', fillcolor='darkolivegreen1')


                g.edge(nodo.texto, valor.texto,label=llaver)
                self.pruebaLR02(deepcopy(valor),g)

        g.save()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin'
        os.system('dot -Tpng Lr0.gv -o Lr0.png')

    def pruebaLR02(self, nodo,g):
        for llaver, valor in nodo.siguientes.items():
            if  valor  is not None:
                g.node(nodo.texto,shape='box', style='filled', fillcolor='darkolivegreen1')
                if valor.siguientes=={}:
                    g.node(valor.texto, shape='box', style='filled', fillcolor='cyan4')

                else:
                    g.node(valor.texto,shape='box',style='filled', fillcolor='darkolivegreen1')
                g.edge(nodo.texto, valor.texto,label=llaver)
                self.pruebaLR02(deepcopy(valor), g)

    def pruebaLR1(self, nodo):
        g = Graph(name='Lr1', format='dot')
        for llaver, valor in nodo.siguientes.items():
            if valor is not None:
                g.node(nodo.textolr1, shape='box', style='filled', fillcolor='darkolivegreen1')
                g.node(valor.textolr1, shape='box', style='filled', fillcolor='darkolivegreen1')
                if valor.siguientes == {}:
                    g.node(valor.textolr1, shape='box', style='filled', fillcolor='cyan4')

                else:
                    g.node(valor.textolr1, shape='box', style='filled', fillcolor='darkolivegreen1')
                g.edge(nodo.textolr1, valor.textolr1, label=llaver)

                self.pruebaLR12(deepcopy(valor), g)

        g.save()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin'
        os.system('dot -Tpng Lr1.gv -o Lr1.png')

    def pruebaLR12(self, nodo, g):
        for llaver, valor in nodo.siguientes.items():
            if valor is not None:

                g.node(nodo.textolr1, shape='box', style='filled', fillcolor='darkolivegreen1')
                g.node(valor.textolr1, shape='box', style='filled', fillcolor='darkolivegreen1')
                if valor.siguientes == {}:
                    g.node(valor.textolr1, shape='box', style='filled', fillcolor='cyan4')

                else:
                    g.node(valor.textolr1, shape='box', style='filled', fillcolor='darkolivegreen1')

                g.edge(nodo.textolr1, valor.textolr1,label=llaver)

                self.pruebaLR12(deepcopy(valor), g)





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
            gramatica.get(noterminal).Ponepuntos()



        return deepcopy(gramatica)

    #se genera el automata con la informacion de la gramatica,


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
                            return False

        return esFinal

    def ponerPuntosYComasGramaticaLr1(self,gramatica):
        for noterminal in gramatica.keys():
            gramatica.get(noterminal).PonepuntosComas()

        return deepcopy(gramatica)





    def  llenarAutomataLR1(self,gramatica):
        gramat=self.OrganizarLR1PuntosSiguientes(deepcopy(gramatica))

        nodito = Nodo(deepcopy(gramat))
        if nodito.textolr1 not in self.listnodoLr1:
            self.listnodoLr1.append(deepcopy(nodito.textolr1))

            if self.verificarFinLr1(deepcopy(gramat)) == False:
                NodoSiguientes=self.recursionLr1(deepcopy(gramat))

                nodito.siguientes=deepcopy(NodoSiguientes)

            return deepcopy(nodito)
        else:
            return deepcopy(nodito)

    def recursionLr1(self,gramatica):
        nodos= {}
        ExpreYaMovida=[]


        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if auxExpresion.strip() == '.':
                        punto = listaExpresion.index(auxExpresion)
                        if punto <len(listaExpresion)-1:
                            siguiente = listaExpresion[punto+1].strip()
                            if siguiente not in ExpreYaMovida:
                                ExpreYaMovida.append(copy(siguiente))
                                nodos[copy(siguiente)]=self.moviendoFilas(deepcopy(gramatica),copy(siguiente))


        return deepcopy(nodos)

    def moviendoFilas(self,gramatica,siguiente):
        gramatica=deepcopy(gramatica)
        gramatica2=deepcopy(gramatica)

        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                cumple=True
                for auxExpresion in listaExpresion:
                    if auxExpresion.strip() == '.':
                        punto = listaExpresion.index(auxExpresion)
                        if punto < len(listaExpresion)-1 and cumple:
                            if listaExpresion[punto +1].strip() ==siguiente:
                                cumple=False
                                gramatica2.get(noterminal).MoverPunto( Expresion,siguiente)



                if cumple:

                    gramatica2.get(noterminal).EliminaExpresion(Expresion)


        return self.llenarAutomataLR1(deepcopy(gramatica2))



    def OrganizarLR1PuntosSiguientes(self,gramatica):
        gramaticaAdicional={}

        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if  auxExpresion.strip()=='.':
                        punto = listaExpresion.index(auxExpresion)
                    # NOterminal
                        if punto + 1 <len(listaExpresion)and listaExpresion[punto + 1].strip() in self.gramaticaaComasPuntos.keys():

                            gramaticaAdicional[listaExpresion[punto + 1].strip()] = deepcopy(self.gramaticaaComasPuntos.get(listaExpresion[punto + 1].strip()))
                            if punto + 2 <len(listaExpresion)-1:
                                if listaExpresion[punto + 2].strip() in self.gramaticaaComasPuntos.keys():
                                    gramaticaAdicional.get(listaExpresion[punto + 1].strip()).agregarExpresionesPrimerosLr1\
                                        (deepcopy(self.gramaticaaComasPuntos.get(listaExpresion[punto + 2].strip()).primeros))

                                else:
                                    gramaticaAdicional.get(listaExpresion[punto + 1].strip()).agregarExpresionPrimeroLr1\
                                        (listaExpresion[punto + 2].strip())

                            else:
                                gramaticaAdicional.get(listaExpresion[punto + 1].strip()).agregarExpresionesPrimerosLr1 \
                                    (deepcopy(gramatica.get(noterminal).ExpresionPrimeroLr1))

        if gramaticaAdicional != {}:

            if self.OrganizarLR1PuntosSiguientes2(deepcopy(gramaticaAdicional)) is not None:
                gramaticaAdicional = deepcopy(self.OrganizarLR1PuntosSiguientes2(deepcopy(gramaticaAdicional)))
            for llaver,valores in gramaticaAdicional.items():
                if llaver in gramatica.keys():
                    gramatica.get(llaver).agregarExpresiones( gramaticaAdicional.get(llaver).expresiones)
                    gramatica.get(llaver).ExpresionPrimeroLr1 = deepcopy(gramaticaAdicional.get(llaver).ExpresionPrimeroLr1)
                else:
                    gramatica[llaver] = deepcopy(valores)


        return deepcopy(gramatica)

    def OrganizarLR1PuntosSiguientes2(self,gramatica):
        gramaticaAdicional={}

        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if  auxExpresion.strip()=='.':
                        punto = listaExpresion.index(auxExpresion)
                    # NOterminal
                        if punto + 1 < len(listaExpresion) and listaExpresion[
                            punto + 1].strip() in self.gramaticaaComasPuntos.keys():

                            gramaticaAdicional[listaExpresion[punto + 1].strip()] = deepcopy(
                                self.gramaticaaComasPuntos.get(listaExpresion[punto + 1].strip()))

                            if punto + 2 < len(listaExpresion) - 1:
                                if listaExpresion[punto + 2].strip() in self.gramaticaaComasPuntos.keys():
                                    gramaticaAdicional.get(
                                        listaExpresion[punto + 1].strip()).agregarExpresionesPrimerosLr1 \
                                        (deepcopy(self.gramaticaaComasPuntos.get(listaExpresion[punto + 2].strip()).primeros))

                                else:
                                    gramaticaAdicional.get(
                                        listaExpresion[punto + 1].strip()).agregarExpresionPrimeroLr1(
                                        listaExpresion[punto + 2].strip())

                            else:
                                gramaticaAdicional.get(listaExpresion[punto + 1].strip()).agregarExpresionesPrimerosLr1 \
                                    (deepcopy(gramatica.get(noterminal).ExpresionPrimeroLr1))
        if gramaticaAdicional != {}:

            if self.OrganizarLR1PuntosSiguientes2(deepcopy(gramaticaAdicional)) is not None:
                gramaticaAdicional=deepcopy(self.OrganizarLR1PuntosSiguientes2(deepcopy(gramaticaAdicional)))
            for llaver, valores in gramaticaAdicional.items():
                if llaver in gramatica.keys():
                    gramatica.get(llaver).agregarExpresiones(gramaticaAdicional.get(llaver).expresiones)
                    gramatica.get(llaver).ExpresionPrimeroLr1 = deepcopy(gramaticaAdicional.get(llaver).ExpresionPrimeroLr1)

                else:
                     gramatica[llaver] = valores
        return deepcopy(gramatica)






















