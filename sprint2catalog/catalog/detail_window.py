import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class DetailWindow(Gtk.Window):

    def __init__(self, image, titulo, label2, lista):
        super().__init__(title=titulo)
        self.titulo= titulo
        self.lista= lista
        self.image= image
        self.connect("destroy", self.on_destroy) #Al cerrar la ventana invoco la función on_destroy
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_position(Gtk.WindowPosition.CENTER)

        self.set_border_width(15)
        self.set_default_size(200, 200)

        box.pack_start(image, True, True, 0)

        box.pack_start(label2, True, True, 0)

        self.add(box)
    def on_destroy(self,event): #con esta función se borra de la lista el título, que es igual al nombre, de la lista
                                #para poder volver a abrir la ventana
        self.lista.remove(self.titulo)

    def get_lista(self):

        return self.lista










