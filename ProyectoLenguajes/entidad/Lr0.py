import entidad.Gramatica;
#clase que hereda de Gramatica
class Lr0(Gramatica):

    def __init__(self,tablaSintactica):
        self.tablaSintactica=tablaSintactica

    def getTablaSintactica(self):
        return self.tablaSintactica

    #metodo que llena la tabla sintactica lr0 y sro
    #es diccionrario que se llena con la informacion de los siguientes y primeros
    def llenarTabla(self):
        print("")


