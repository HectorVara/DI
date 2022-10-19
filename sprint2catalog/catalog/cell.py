import gi
from gi.repository import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from detail_window import DetailWindow
class Cell(Gtk.EventBox):
    def __init__(self, name, image):
     super().__init__()
     self.name=name

     self.image=image
     self.titulo=name
     self.label2 = Gtk.Label("Logo de los "+name)
     box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
     box.pack_start(Gtk.Label(label=name), False, False, 0)
     box.pack_start(image, True, True, 0)
     self.add(box)
     self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        image = Gtk.Image()
        image.set_from_pixbuf(self.image.get_pixbuf())
        dwin= DetailWindow(image, self.titulo, self.label2)
        dwin.show_all()





