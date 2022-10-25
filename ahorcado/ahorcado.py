import random

import gi
import requests, threading, shutil
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class juegoAhorcado(Gtk.Window):
    image = Gtk.Image.new_from_file("C:\\msys64\\home\\Hector\\DI\\ahorcado\\resources\\1.png")
    entry = Gtk.Entry()
    entry.set_max_length(1)
    fallos = 0
    letras = ""
    letrero = ""
    letraJugada=""
    nuestraPalabra=""
    palabras = ["bart", "homer", "marge", "lisa", "maggie", "milhouse", "krusty", "skinner", "otto", "smithers",
                "burns"]
    elegida = palabras[random.randint(0, len(palabras) - 1)]
    label = Gtk.Label()
    for i in elegida:
        letrero = letrero + " __"

    label.set_text(letrero)

    def __init__(self):
        super().__init__(title="Ahorcado de los Simpson")
        self.set_border_width(15)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        self.entry.set_text("Texto aqui...")
        button= Gtk.Button("Juega")
        button.connect("clicked", self.on_button_clicked)


        self.add(box)
        box.pack_start(self.label, True, True, 0)
        box.pack_start(self.image, True, True, 0)
        box.pack_start(box2, True, True, 0)
        box2.pack_start(self.entry, True, True, 0)
        box2.pack_start(button, True, True, 0)

    def on_button_clicked(self):
        self.letraJugada= self.entry.get_text()
        while not self.hasGanado() or self.fallos <6:
            self.comprobarJugada(self.letraJugada, self.elegida)



    def hasGanado(self):
        if self.elegida == self.jugada:
            return True
        else:
            return False
    def comprobarJugada(self, letra, elegida):

        for i in elegida:
            if letra == elegida[i]:
                self.letrero[i] = letra
            else:

                self.fallos += 1
        self.label.set_text(self.letrero)
    def cargarImagen(self, fallos, imagen):
        self.image=





