import gi
import requests, threading, shutil
from gi.repository import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GLib
from cell import Cell

class MainWindow(Gtk.Window):

    flowbox= Gtk.FlowBox()
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
        filem = Gtk.MenuItem("Ayuda")
        filem.set_submenu(filemenu)

        exit = Gtk.MenuItem("Acerca de")
        #exit.connect("activate",acercaDeMi())
        filemenu.append(exit)

        mb.append(filem)

        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        scrolled= Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(vbox)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        for item in data_source:
            cell= Cell(item.get("name"), item.get("gtk_image"))
            self.flowbox.add(cell)


    def acercaDeMi(self):
        De