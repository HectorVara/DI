import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class DetailWindow(Gtk.Window):


    def __init__(self, image, titulo, label2):
        super().__init__(title=titulo)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_position(Gtk.WindowPosition.CENTER)

        self.set_border_width(15)
        self.set_default_size(200, 200)

        box.pack_start(image, True, True, 0)

        box.pack_start(label2, True, True, 0)

        self.add(box)



