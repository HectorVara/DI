import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class YesWindow(Gtk.Window):
    label=Gtk.Label("Has pulsado si")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    def __init__(self):
        #Añadimos la box y le metemos el label con el mensaje
        super().__init__(title="YES")
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
