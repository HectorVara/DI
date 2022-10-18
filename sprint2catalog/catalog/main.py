import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow
from detail_window import DetailWindow


"""dwin= DetailWindow(Gtk.Image.new_from_file("data/edited/Suns.jpg"), Gtk.Label("Hornets"),Gtk.Label("Logo Hornets"))
dwin.show_all()"""
win = MainWindow()
win.show_all()
Gtk.main()

