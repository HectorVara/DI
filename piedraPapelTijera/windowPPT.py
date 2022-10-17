import gi
from gi.repository import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class WindowPPT(Gtk.Window):

    flowbox= Gtk.FlowBox()
    def __init__(self):
        super().__init__(title="Piedra, papel, tijera")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header=Gtk.HeaderBar(title="Juego")
        header.set_subtitle("Escoge una jugada")
        header.props.show_close_button= True

        self.set_titlebar(header)

        scrolled= Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        paper = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\paper.png", 200, 200, False)
        paper.set_from_pixbuf(pixbuf)
        cell_one= Cell("paper", paper)

        rock = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\rock.png", 200, 200, False)
        rock.set_from_pixbuf(pixbuf)
        cell_two = Cell("rock", rock)

        scissors=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("C:\\msys64\\home\\Hector\\DI\\piedraPapelTijera\\resources\\scissors.png", 200, 200, False)
        scissors.set_from_pixbuf(pixbuf)
        cell_three = Cell("scissors", scissors)



        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)