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


