
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

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.button1.connect("clicked", self.on_button1_clicked)
        self.button2.connect("clicked", self.on_button2_clicked)

        self.add(self.box)


        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.box2, True, True, 0)
        self.box2.pack_start(self.button1, True, True, 0)
        self.box2.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, button1):

        yesWindow=YesWindow()

        yesWindow.show_all()

    def on_button2_clicked(self, button2):
        noWindow = NoWindow()

        noWindow.show_all()
