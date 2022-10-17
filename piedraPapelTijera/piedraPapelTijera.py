import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from windowPPT import WindowPPT
win = WindowPPT()
win.show_all()
Gtk.main()