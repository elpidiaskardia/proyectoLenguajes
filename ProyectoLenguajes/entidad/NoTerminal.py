#clase terminal de una gramatica
class NoTerminal:

    #@param nombre calor del terminar,
    #@param siguientes son los siguientes del terminal almacenados en una lista de str
    #@param primeros son los primeros del terminal almacenados en una lista de str


    def __init__(self,nombre):
        self.nombre=nombre
        self.expresiones = []
        self.siguientes=[]
        self.primeros=[]

    #metodo que agraga a al diccionario de siguientes un siguiente el siguiente de
    #este terminal, retorna un booleano si se ha agregao con exito,
    #false en caso de no serlo
    def agregarSiguientes(self,siguiente):
        for auxiliar_siguiente in siguiente:
            if  auxiliar_siguiente not in self.siguientes:
                self.siguientes.append(auxiliar_siguiente)

     #metodo que agrega a la lista de str de primeros, los primeros de este terminal
    #retorna un true sde ser exitoso o un false de no serlo
    def agregarPrimero(self,primero):
        for auxiliar_primero in primero:
            if  auxiliar_primero not in self.primeros:
                self.primeros.append(auxiliar_primero)

