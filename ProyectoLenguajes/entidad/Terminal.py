#clase terminal de una gramatica
class Terminal:

    #@param nombre calor del terminar,
    #@param siguientes son los siguientes del terminal almacenados en una lista de str
    #@param primeros son los primeros del terminal almacenados en una lista de str

    def __init__(self,nombre,siguientes,primeros):
        self.nombre=nombre
        self.siguientes=siguientes
        self.primeros=primeros

    #metodo que agraga a al diccionario de siguientes un siguiente el siguiente de
    #este terminal, retorna un booleano si se ha agregao con exito,
    #false en caso de no serlo
    def agregarSiguientes(self,siguiente):
        print("")

     #metodo que agrega a la lista de str de primeros, los primeros de este terminal
    #retorna un true sde ser exitoso o un false de no serlo
    def agregarPrimero(self,pimero):
        print("")