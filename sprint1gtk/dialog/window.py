
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from no_window import NoWindow
from yes_window import YesWindow
class MainWindow(Gtk.Window):
    box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    label=Gtk.Label("Pulse si o no")
    button1=Gtk.Button(label="Si")
    button2 = Gtk.Button(label="No")
    #Declaramos los atributos de la clase, posicionamos las boxes y la damos valor a la label y a las etiquetas de los botones
    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)#Al cerrar la ventana principal se cierra todo
        self.button1.connect("clicked", self.on_button1_clicked)
        self.button2.connect("clicked", self.on_button2_clicked)
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.box2, True, True, 0)#Añadimos la box2 a la box
        self.box2.pack_start(self.button1, True, True, 0)
        self.box2.pack_start(self.button2, True, True, 0)#y añadimos los botones a la box2

    def on_button1_clicked(self, button1):
        #Al pulsar el botón 1 invocamos la YesWindow
        yesWindow=YesWindow()

        yesWindow.show_all()

    def on_button2_clicked(self, button2):
        # Al pulsar el botón 2 invocamos la NoWindow
        noWindow = NoWindow()

        noWindow.show_all()
