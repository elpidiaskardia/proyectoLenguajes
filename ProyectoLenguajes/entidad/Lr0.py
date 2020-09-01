#clase que hereda de Gramatica
from ..entidad.Nodo import Nodo

from copy import *
class Lr0():
    listnodoLr = []

    def __init__(self,gramatica):
        self.gramatica=gramatica
        self.tablaSintactica=[]
        self.Principanodo=''


    def Crea(self):
        self.Principanodo=deepcopy(self.llenarAutomataLR02(deepcopy(self.gramatica)))
    def getTablaSintactica(self):
        return self.tablaSintactica

    #metodo que llena la tabla sintactica lr0 y sro
    #es diccionrario que se llena con la informacion de los siguientes y primeros
    def llenarTabla(self):
        print("")
    def llenarAutomataLR02(self, gramatica):


        nodito = Nodo(deepcopy(gramatica))

        if self.verificarFinLro(deepcopy(gramatica)) == False:
                NodoSiguientes = self.recursionLr0(deepcopy(gramatica))

                nodito.siguientes = deepcopy(NodoSiguientes)

        return nodito


    def  llenarAutomataLR0(self,gramatica):
        gramat=self.OrganizarLR0PuntosSiguientes(deepcopy(gramatica))
        gramat = self.OrganizarLR0PuntosSiguientes(deepcopy(gramat))
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
                                dd= gramatica.get(noterminal).expresiones[ubicacionExpresion]

                                gramatica2.get(noterminal).MoverPunto( Expresion,siguiente)
                                dd= gramatica.get(noterminal).expresiones[ubicacionExpresion]


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
                        if punto + 1 <len(listaExpresion)and listaExpresion[punto + 1].strip() in gramatica.keys():
                            gramaticaAdicional[listaExpresion[punto + 1].strip()] = self.gramatica.get(listaExpresion[punto + 1].strip())
                            # siguen los llamados recursivos y listo papus ;v
        for llaver,valores in gramaticaAdicional.items():
            gramatica[llaver] =valores

        return deepcopy(gramatica)



    def verificarFinLro(self,gramatica):
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                listaExpresion = Expresion.split(' ')
                if listaExpresion[len(listaExpresion)-1].strip()!='.' :

                    return False

        return True


