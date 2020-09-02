#clase nodo que representa los estado de un automata
class Nodo:

    #contructor cdel nodo co valores y relaciones
    #@param relaciones es un diccionario con las relaciones de este nodo con otros nodos
    #@param valores son el diccionario con el valore o nombre del nodo, los fragmentos de la gramatica

    def __init__(self,gramatica):
        self.gramatica=gramatica
        self.siguientes={}
        self.texto=self.textoNodo(gramatica)
        self.textolr1=self.textoNodolr1(gramatica)

    def getValores(self):
        return self.valores

    def getRelaciones(self):
        return self.relaciones
    def textoNodo(self,gramatica):
        texto=''
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                texto += noterminal+ '-> ' +Expresion+'\n'

        return texto


    def textoNodolr1(self,gramatica):
        texto=''
        for noterminal in gramatica.keys():
            for Expresion in gramatica.get(noterminal).expresiones:
                texto += noterminal+ '-> ' +Expresion + gramatica.get(noterminal).textoPrimeroExpre() +'\n'

        return texto