import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
class DetailWindow(Gtk.Window):


    resultado=""

    def __init__(self, image, imagecpu, jugadaUsuario, jugadaCPU):
        label = Gtk.Label("")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        super().__init__(title="Piedra, papel, tijera")
        self.set_border_width(15)
        self.set_default_size(200, 200)
        if jugadaCPU == jugadaUsuario:
            self.resultado = "Empate"
        elif jugadaCPU == "rock" and jugadaUsuario=="scissors":
            self.resultado= "Gana la CPU"
        elif jugadaCPU == "paper" and jugadaUsuario == "rock":
            self.resultado= "Gana la CPU"
        elif jugadaCPU== "scissors" and jugadaUsuario== "paper":
            self.resultado= "Gana la CPU"
        else:
            self.resultado= "Has ganado!!"


        label.set_text(self.resultado)
        self.add(box)
        box.pack_start(label, True, True, 0)
        box.pack_start(box2, True, True, 0)
        box2.pack_start(image, True, True, 0)
        box2.pack_start(imagecpu, True, True, 0)
