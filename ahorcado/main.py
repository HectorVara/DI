import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ahorcado import juegoAhorcado

nuevo= juegoAhorcado()
nuevo.show_all()
Gtk.main()