import gi
from gi.overrides import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import DetailWindow
class Cell(Gtk.EventBox):
    name= None
    image=None
    label1=None
    label2=None
    def __init__(self, name, image):
     super().__init__()
     self.name=name

     self.image=image
     self.label1=Gtk.Label(name)
     self.label2 = Gtk.Label("Logo de los "+name)
     box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
     box.pack_start(Gtk.Label(label=name), False, False, 0)
     box.pack_start(image, True, True, 0)
     self.add(box)
     self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        image = self.asignarImagen(self.name)
        dwin= DetailWindow(image, self.label1, self.label2)
        dwin.show_all()

    def asignarImagen(self, name):
        image = Gtk.Image()
        pixbuf = None
        if name == "Suns":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Suns.jpg", 200, 200, False)

        elif name == "Hornets":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Hornets.png", 200, 200, False)

        elif name == "Nets":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Nets.jpg", 200, 200, False)

        elif name == "Raptors":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Raptors.jpg", 200, 200, False)

        else:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Spurs.png", 200, 200, False)


        image.set_from_pixbuf(pixbuf)
        return image





