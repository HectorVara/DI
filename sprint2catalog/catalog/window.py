import gi
import requests, threading, shutil
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GLib
from cell import Cell
from detail_window import DetailWindow

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()
    lista= []
    def __init__(self, data_source):
        super().__init__(title="NBA")

        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(700, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

        header=Gtk.HeaderBar(title="Equipos")
        header.set_subtitle("Algunos equipos")
        header.props.show_close_button= True

        self.set_titlebar(header)
        mb = Gtk.MenuBar()
        filemenu = Gtk.Menu()
        ayuda = Gtk.MenuItem("Ayuda")
        ayuda.set_submenu(filemenu)

        acerca = Gtk.MenuItem("Acerca de")
        acerca.connect("button-release-event",self.on_click)
        filemenu.append(acerca)

        mb.append(ayuda)
        scrolled= Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(scrolled, True, True, 0)
        scrolled.add(self.flowbox)
        self.add(vbox)


        for item in data_source:
            cell= Cell(item.get("name"), item.get("gtk_image"))
            self.flowbox.add(cell)

    def on_click(self, widget, event): #Aquí repito el proceso para que no se abra esta ventana varias veces
        name= "Acerca de mi"
        image_url = "https://github.com/HectorVara/DI/blob/master/api-rest/edited/The-Big-Lebowski.jpeg?raw=true"
        r = requests.get(image_url, stream=True)
        with open("temp.png", "wb") as f:
            shutil.copyfileobj(r.raw, f)
        image = Gtk.Image.new_from_file("temp.png")
        if name not in self.lista:
            self.lista.append(name)
            dwin= DetailWindow(image, "Acerca de mi", Gtk.Label("The Dude abides, Cheers!"),self.lista)

            dwin.show_all()
        lista = DetailWindow.get_lista