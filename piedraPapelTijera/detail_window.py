import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
class DetailWindow(Gtk.Window):
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    label= Gtk.Label("")
    resultado=""

    def __init__(self, image, imagecpu, jugadaUsuario, jugadaCPU):
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


        self.label.set_text(self.resultado)
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.box2, True, True, 0)
        self.box2.pack_start(image, True, True, 0)
        self.box2.pack_start(imagecpu, True, True, 0)
