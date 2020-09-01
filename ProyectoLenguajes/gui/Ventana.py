from tkinter import *
import os

from tkinter import  filedialog
from tkinter import *
from tkinter.simpledialog import *
import Animacion

from subprocess import check_call


from entidad.Gramatica import  Gramatica

#bloque que representa la ventana que ve el usuario, utiliza los metodos de control gramatica
#para realizar las operaciones de los botones


gramatica=Gramatica()
# bloque que representa la ventana que ve el usuario, utiliza los metodos de control gramatica
# para realizar las operaciones de los botones

# metodo que pide al usuario subir un archivo de texto para obtener la gramatica
def cargarGramatica():
    direccion = filedialog.askopenfilename()
    gramatica.leerGramatica(direccion)

    


# metodo que genera el automata de la gramatica lr0
def generarAutomataLr0():
    #gramatica.ponerPuntosGramatica()
    #gramatica.llenarAutomataLR0()
    print('')


# metodo que genera el automata de la gramatica lr1
def generarAutomataLr1():
    print("")


# metodo que muestra la tabla de la gramatica lr0
def generarTablaLr0():
    print("")


# Ventana
root = Tk()
root.geometry('1100x650')
root.title('Automata Gramatica')
root.configure(background='DodgerBlue4')

# VS-> ventana de animacion
vs = Frame(root, width=900, height=650)
vs.config(bg="black")
# unir pygame con tkintetr

os.environ['SDL_WINDOWID'] = str(vs.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
anime = Animacion

# VE-> ventana de eventos
ve = Frame(root, width=200, height=650)
ve.config(bg="DodgerBlue4")


# fdistribucion de los frame para la animacion y ventana
ve.grid(column=1, row=0)
vs.grid(column=2, row=0)

# configruaracion label
cargarGramaticaLabel = Label(ve, text="Cargar Gramatica", fg='lavender', bg='DodgerBlue4', font='Fixedsys 18')
cargarGramaticaLabel.grid(column=0, row=0, padx=15, pady=5, sticky='n', columnspan='2')

automatasLabel = Label(ve, text="Automatas", fg='lavender', bg='DodgerBlue4', font='Fixedsys 18')
automatasLabel.grid(column=0, row=2, padx=15, pady=5, sticky='n', columnspan='2')

tablaLabel = Label(ve, text="Tabla Sintactica", fg='lavender', bg='DodgerBlue4', font='Fixedsys 18')
tablaLabel.grid(column=0, row=5, padx=15, pady=5, sticky='n', columnspan='2')

# configuracion botones
cargarGramaticaButton = Button(ve, text="Cargar", fg='white', background='tomato', font='Fixedsys 16',
                               command=cargarGramatica)
cargarGramaticaButton.grid(column=0, row=1, padx=5, pady=5, sticky='n', columnspan='2')
cargarGramaticaButton.config(width=15, height=0)

generarAutomataLr0Button = Button(ve, text="Automata LR0", fg='white', background='gray51', font='Fixedsys 16',
                                  command=generarAutomataLr0)
generarAutomataLr0Button.grid(column=0, row=3, padx=5, pady=5, sticky='n', columnspan='2')
generarAutomataLr0Button.config(width=15, height=0)

generarAutomataLr1Button = Button(ve, text="Automata LR1", fg='white', background='sea green', font='Fixedsys 16',
                                  command=generarAutomataLr1)
generarAutomataLr1Button.grid(column=0, row=4, padx=5, pady=5, sticky='n', columnspan='2')
generarAutomataLr1Button.config(width=15, height=0)

generarTablaLr0Button = Button(ve, text="Tabla LR0", fg='white', background='navy', font='Fixedsys 16',
                               command=generarTablaLr0)
generarTablaLr0Button.grid(column=0, row=6, padx=5, pady=5, sticky='n', columnspan='2')
generarTablaLr0Button.config(width=15, height=0)

canvas = Canvas(root, width = 300, height = 300)






root.mainloop()

