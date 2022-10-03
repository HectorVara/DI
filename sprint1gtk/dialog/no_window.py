import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NoWindow(Gtk.Window):
    box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    label=Gtk.Label("Has pulsado no")

    def __init__(self):
        super().__init__(title="NO")
        self.connect("destroy", Gtk.main_quit)
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
