
#clase principal que realizara la mayor parte de la logica,
#este pasara esta logica a ventana para mostrarlo al usuario'''
class ControlGramatica:


#constructor que recibe la gramatica de la clase Gramatica

    def _init_(self,gramatica):
        self.gramatica=gramatica;


#metodo que genera la tabla sintactca de la gramatica lr0
#@:param tabla dicciorario de la clase Tabla por asi decirlo una matrz

    def generarTabla(self,tabla):
        print("");
