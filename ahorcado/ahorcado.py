import gi
import requests, threading, shutil
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class juegoAhorcado(Gtk.Window):
    def __init__(self):
        box= Gtk.Box
        label= Gtk.Label
        entry= Gtk.Entry
        image= Gtk.Image
        fallos=0
        letras=""