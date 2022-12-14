import random

import gi
import requests, threading, shutil
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class juegoAhorcado(Gtk.Window):
    image = Gtk.Image()
    entry = Gtk.Entry()
    entry.set_max_length(1)#Solo se permite introducir un caracter
    fallos = 0
    letras = ""
    letrero = [] #Aquí se ve las los barras bajas o letras según se vaya acertando
    letreroString="" #La variable lista anterior que luego se pasa a string para comparar con la elegida
    letraJugada=""#La letra elegida por el usuario
    letrasUsadas=""#las letras que se van utilizando
    nuestraPalabra=""
    palabras = ["bart", "homer", "marge", "lisa", "maggie", "milhouse", "krusty", "skinner", "otto", "smithers",
                "burns"]
    elegida = palabras[random.randint(0, len(palabras) - 1)]
    #print(elegida) Para realizar pruebas conociendo la palabra elegida al azar
    label = Gtk.Label()
    letrasJugadas=Gtk.Label()
    numeroFallos= Gtk.Label()
    button = Gtk.Button("Juega")


    ficheroJson= []

    def __init__(self, data_source):
        """En el cosntructor se diseña la ventana del juego y sus elementos
        El letrero se usa como lista porque es más fácil intercambiar letras y luego se pasa a string
        para insertarlo en el Label"""
        super().__init__(title="Ahorcado de los Simpson")
        self.set_border_width(15)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.entry.set_text("")

        self.button.connect("clicked", self.on_button_clicked)


        self.add(box)
        box.pack_start(self.label, True, True, 0)
        box.pack_start(self.image, True, True, 0)
        box.pack_start(self.letrasJugadas, True, True, 0)
        box.pack_start(self.numeroFallos, True, True, 0)
        box.pack_start(box2, True, True, 0)
        box2.pack_start(self.entry, True, True, 0)
        box2.pack_start(self.button, True, True, 0)

        self.ficheroJson= data_source
        self.fallos = 0
        self.cargarImagen()

        for i in range(len(self.elegida)):
            self.letrero.append("__ ")
        self.listaToString()
        self.label.set_text(self.letreroString)

    def listaToString(self):
        self.letreroString=""
        for i in range (len(self.letrero)):
            self.letreroString += self.letrero[i]

    def on_button_clicked(self, widget):

        self.letraJugada = self.entry.get_text()
        self.letrasUsadas += self.letraJugada#Se añade la letra escrita en el Entry a la cadena para abajo añadirla a la Label
        self.entry.set_text("")

        self.letrasJugadas.set_text(self.letrasUsadas)
        self.comprobarJugada(self.letraJugada, self.elegida, self.letrero)
        self.cargarImagen()
        self.comprobarResultado()

    def comprobarResultado(self):
        #Aquí se comprueba si el usuario ha ganado o perdido y se termina la partida desactivando el botón
        if self.elegida == self.letreroString:
            self.label.set_text("HAS GANADO!!")
            self.button.set_sensitive(False)

        if self.fallos > 5:
            self.label.set_text("HAS PERDIDO :(")
            self.button.set_sensitive(False)


    def comprobarJugada(self, letra, elegida,letrero):
        acierto= False
        # Se comprueba la letra jugada y si hay coincdencia se muestra en la Label
        for i in range (len(elegida)):
            if letra == elegida[i]:
                letrero[i] = letra
                self.listaToString()
                self.label.set_text(self.letreroString)
                acierto= True


        # Si no hay coincidencia se suma un fallo y se muestra
        if not acierto:
            self.fallos += 1
            self.numeroFallos.set_text("Fallos: "+str(self.fallos))

    def cargarImagen(self):

            for item in self.ficheroJson:

                if self.fallos == item.get("fallos"):

                    self.image.set_from_pixbuf(item.get("gtk_image").get_pixbuf())









