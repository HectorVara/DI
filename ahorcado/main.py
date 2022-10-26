import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ahorcado import juegoAhorcado
from  loadWindow import LoadWindow

nuevo= LoadWindow()
nuevo.show_all()
Gtk.main()