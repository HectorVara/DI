import random

import gi
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import DetailWindow
class Cell(Gtk.EventBox):
    name= None
    image=None
    lista=None
    jugadaCPU= None
    def __init__(self, name, image):
     super().__init__()
     self.name=name
     self.image=image
     box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
     box.pack_start(Gtk.Label(label=name), False, False, 0)
     box.pack_start(image, True, True, 0)
     self.add(box)
     self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
         lista = ["rock", "paper", "scissors"]
         jugadaCPU= lista[random.randint(0, 2)]
         image = self.asignarImagen(self.name)
         imagecpu= self.asignarImagenCPU(jugadaCPU)

         dwin = DetailWindow(image, imagecpu, self.name, jugadaCPU)
         dwin.show_all()

    def asignarImagen(self, name):
         image = Gtk.Image()
         pixbuf = None
         if name == "paper":
             pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\paper.png", 100, 100, False)

         elif name == "rock":
             pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\rock.png", 100, 100, False)

         elif name == "scissors":
             pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\scissors.png", 100, 100, False)


         image.set_from_pixbuf(pixbuf)
         return image

    def asignarImagenCPU(self, jugadaCPU):
         imagecpu = Gtk.Image()
         pixbuf = None
         if jugadaCPU == "paper":
             pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\paperCPU.png", 100, 100, False)

         elif jugadaCPU == "rock":
             pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\rockCPU.png", 100, 100, False)

         elif jugadaCPU == "scissors":
             pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\scissorsCPU.png", 100, 100, False)


         imagecpu.set_from_pixbuf(pixbuf)
         return imagecpu