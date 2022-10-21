import gi
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from detail_window import DetailWindow
class Cell(Gtk.EventBox):
    lista = [] #En ésta lista voy a meter los nombres de las ventanas abiertas
    def __init__(self, name, image):#En el constructor inicializamos los parámetros
     super().__init__()
     self.name=name
     self.image=image
     self.titulo=name

     self.label2 = Gtk.Label("Logo de los "+name)
     box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
     box.pack_start(Gtk.Label(label=name), False, False, 0)
     box.pack_start(image, True, True, 0) #Metemos en la box los elementos y ésta en la EventBox Cell
     self.add(box)
     self.connect("button-release-event", self.on_click)#Conectamos la EventBox con la función on_click

    def on_click(self, widget, event):

        image = Gtk.Image()
        image.set_from_pixbuf(self.image.get_pixbuf())

        if self.name not in self.lista:
            self.lista.append(self.name)
            dwin= DetailWindow(image, self.titulo, self.label2,self.lista) #Aquí se invoca una ventana tipo DetailWindow que muestra
                                                            #la imagen, título y la etiqueta
            dwin.show_all()
        lista = DetailWindow.send_lista #Recojo la lista para ver si se ha cerrado alguna






