#clase que hereda de Gramatica
from ..entidad.Nodo import Nodo

from copy import *
class Lr0():
    listnodoLr = []

    def __init__(self,gramatica):
        self.gramatica=gramatica
        self.tablaSintactica=[[]]
        self.TerminalesYNoterminales=[]
        self.Principanodo=''
    # [][id][S][A][]
    # [1]
    # [2]
    # [3]


    def tabla(self):



        self.Espresiones2(self.Principanodo)
        self.TerminalesYNoterminales.append('$')

        for espresciones in self.TerminalesYNoterminales:
            self.tablaSintactica[0].append(espresciones)
        for estados in self.listnodoLr:
            self.tablaSintactica.append([self.listnodoLr.index(estados)])
            for x in range(len(self.TerminalesYNoterminales)-1):
                self.tablaSintactica[self.listnodoLr.index(estados)+1].append('')

        self.llenarTabla(self.Principanodo)

        for filas in self.tablaSintactica:
                    print(self.tablaSintactica[self.tablaSintactica.index(filas)])

        # metodo que llena la tabla sintactica lr0 y sro
        # es diccionrario que se llena con la informacion de los siguientes y primeros
    def llenarTabla(self,nodo):
        for llaver, valor in nodo.siguientes.items():
            if  nodo.texto in self.listnodoLr:
                self.tablaSintactica[self.listnodoLr.index(nodo.texto)+1][self.tablaSintactica[0].index(llaver)]=self.listnodoLr.index(valor.texto)

            self.llenarTabla(deepcopy(valor))
            print("")

    def Expresiones(self,gramatica):
        expresiones=[]
        for noteminal in gramatica.keys():
            for Expresion in gramatica.get(noteminal).expresiones:
                auxExpresion = Expresion.split(' ')
                for  expresion in auxExpresion:
                    if expresion.strip() !='.':
                        if expresion.strip() not in self.TerminalesYNoterminales:
                            self.TerminalesYNoterminales.append(expresion.strip())



        return expresiones

    def Espresiones2(self, nodo):
        for llaver, valor in nodo.siguientes.items():
            self.Expresiones(valor.gramatica)
            self.Espresiones2(deepcopy(valor))


    def Crea(self):
        self.Principanodo=deepcopy(self.llenarAutomataLR02(deepcopy(self.gramatica)))
        self.tabla()


    def getTablaSintactica(self):
        return self.tablaSintactica





    def llenarAutomataLR02(self, gramatica):


        nodito = Nodo(deepcopy(gramatica))
        self.listnodoLr.append(deepcopy(nodito.texto))
        if self.verificarFinLro(deepcopy(gramatica)) == False:
                NodoSiguientes = self.recursionLr0(deepcopy(gramatica))

                nodito.siguientes = deepcopy(NodoSiguientes)

        return nodito


    def  llenarAutomataLR0(self,gramatica):
        gramat=self.OrganizarLR0PuntosSiguientes(deepcopy(gramatica))

        nodito = Nodo(deepcopy(gramat))
        if nodito.texto not in self.listnodoLr:
            self.listnodoLr.append(deepcopy(nodito.texto))

            if self.verificarFinLro(deepcopy(gramat)) == False:
                NodoSiguientes=self.recursionLr0(deepcopy(gramat))

                nodito.siguientes=deepcopy(NodoSiguientes)

            return deepcopy(nodito)
        else:
            return deepcopy(nodito)

    def recursionLr0(self,gramatica):
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
                                ubicacionExpresion = gramatica.get(noterminal).expresiones.index(Expresion)
                                gramatica2.get(noterminal).MoverPunto( Expresion,siguiente)



                if cumple:

                    gramatica2.get(noterminal).EliminaExpresion(Expresion)


        return self.llenarAutomataLR0(deepcopy(gramatica2))

    def OrganizarLR0PuntosSiguientes(self,gramatica):
        gramaticaAdicional={}

        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if  auxExpresion.strip()=='.':
                        punto = listaExpresion.index(auxExpresion)
                    # NOterminal
                        if punto + 1 <len(listaExpresion)and listaExpresion[punto + 1].strip() in self.gramatica.keys():
                           gramaticaAdicional[listaExpresion[punto + 1].strip()] = deepcopy(
                                    self.gramatica.get(listaExpresion[punto + 1].strip()))

                            # siguen los llamados recursivos y listo papus ;v

        gramaticaAdicional=deepcopy(self.OrganizarLR0PuntosSiguientes2(deepcopy(gramaticaAdicional)))
        for llaver,valores in gramaticaAdicional.items():
            if llaver in gramatica.keys():
                gramatica.get(llaver).agregarExpresiones( gramaticaAdicional.get(llaver).expresiones)
            else:
                gramatica[llaver] = valores


        return deepcopy(gramatica)

    def OrganizarLR0PuntosSiguientes2(self,gramatica):
        gramaticaAdicional={}

        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                for auxExpresion in listaExpresion:
                    if  auxExpresion.strip()=='.':
                        punto = listaExpresion.index(auxExpresion)
                    # NOterminal
                        if punto + 1 <len(listaExpresion)and listaExpresion[punto + 1].strip() in self.gramatica.keys():
                            if listaExpresion[punto + 1].strip() in gramatica.keys():
                                gramatica.get(listaExpresion[punto + 1].strip()).agregarExpresiones(self.gramatica.get(listaExpresion[punto + 1].strip()).expresiones)
                            else:
                                gramaticaAdicional[listaExpresion[punto + 1].strip()] = deepcopy(self.gramatica.get(listaExpresion[punto + 1].strip()))

        if gramaticaAdicional!={}:

            if self.OrganizarLR0PuntosSiguientes2(deepcopy(gramaticaAdicional)) is not None:
                gramaticaAdicional=deepcopy(self.OrganizarLR0PuntosSiguientes2(deepcopy(gramaticaAdicional)))
            for llaver, valores in gramaticaAdicional.items():
                if llaver in gramatica.keys():
                    gramatica.get(llaver).agregarExpresiones(gramaticaAdicional.get(llaver).expresiones)
                else:
                     gramatica[llaver] = valores
        return deepcopy(gramatica)


    def verificarFinLro(self,gramatica):
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                if listaExpresion[len(listaExpresion)-1].strip()!='.' :

                    return False

        return True


