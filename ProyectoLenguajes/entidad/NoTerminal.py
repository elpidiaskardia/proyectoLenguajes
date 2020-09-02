#clase terminal de una gramatica
from copy import *
class NoTerminal:

    #@param nombre calor del terminar,
    #@param siguientes son los siguientes del terminal almacenados en una lista de str
    #@param primeros son los primeros del terminal almacenados en una lista de str


    def __init__(self,nombre):
        self.nombre=nombre
        self.expresiones = []
        self.siguientes=[]
        self.primeros=[]
        self.ExpresionPrimeroLr1 = []

    #metodo que agraga a al diccionario de siguientes un siguiente el siguiente de
    #este terminal, retorna un booleano si se ha agregao con exito,
    #false en caso de no serlo
    def MoverPunto(self,Expresion,siguiente):
        espresion = deepcopy(self.expresiones[ self.expresiones.index(Expresion)])
        ubicacion_punto= espresion.index('.')
        ubicacion_siguiente =espresion[ubicacion_punto:].index(siguiente)
        cantida_siguiente=len(siguiente)

        self.expresiones[self.expresiones.index(Expresion)]= espresion[:ubicacion_punto]+' '+siguiente+' .'+espresion[ubicacion_punto+2+cantida_siguiente:]


    def PonepuntosComas(self):
        for espresion in self.expresiones:
            self.expresiones[self.expresiones.index(espresion)]='. '+espresion+' ,'

    def Ponepuntos(self):
        for espresion in self.expresiones:
            self.expresiones[self.expresiones.index(espresion)]='. '+espresion

    def EliminaExpresion(self,Expresion):

        self.expresiones.pop(self.expresiones.index(Expresion))
    def agregarExpresiones(self,Expresiones):
        for auxiliar_expresion in Expresiones:
            if  auxiliar_expresion not in self.expresiones:
                    self.expresiones.append(auxiliar_expresion)

    def agregarSiguiente(self, siguiente):
            if siguiente not in self.siguientes:
                self.siguientes.append(siguiente)


    def agregarSiguientes(self,siguientes):
        for auxiliar_siguiente in siguientes:
                self.agregarSiguiente(auxiliar_siguiente)

     #metodo que agrega a la lista de str de primeros, los primeros de este terminal
    #retorna un true sde ser exitoso o un false de no serlo
    def agregarPrimero(self,primero):
        if  primero not in self.primeros:
                self.primeros.append(primero)

    def agregarPrimeros(self,primeros):
        for auxiliar_primero in primeros:
            self.agregarPrimero(auxiliar_primero)

    def agregarExpresionPrimeroLr1(self,ExpresionPrimeroLr1):
        if  ExpresionPrimeroLr1 not in self.ExpresionPrimeroLr1:
                self.ExpresionPrimeroLr1.append(ExpresionPrimeroLr1)

    def agregarExpresionesPrimerosLr1(self,ExpresionPrimeroLr1):
        for AuxExpresionPrimeroLr1 in ExpresionPrimeroLr1:
            self.agregarExpresionPrimeroLr1(AuxExpresionPrimeroLr1)
    def textoPrimeroExpre(self):
        text =' { '
        for  primero  in self.ExpresionPrimeroLr1:
            text+=  primero+' '

        text+='} '
        return text






