import gi
from gi.overrides.GdkPixbuf import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class MainWindow(Gtk.Window):

    flowbox= Gtk.FlowBox()
    def __init__(self):
        super().__init__(title="NBA")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header=Gtk.HeaderBar(title="Equipos")
        header.set_subtitle("Algunos equipos")
        header.props.show_close_button= True

        self.set_titlebar(header)

        scrolled= Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        suns = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Suns.jpg", 200, 200, False)
        suns.set_from_pixbuf(pixbuf)
        cell_one= Cell("Suns", suns)

        hornets = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Hornets.png", 200, 200, False)
        hornets.set_from_pixbuf(pixbuf)
        cell_two = Cell("Hornets", hornets)

        nets=Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Nets.jpg", 200, 200, False)
        nets.set_from_pixbuf(pixbuf)
        cell_three = Cell("Nets", nets)

        raptors = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Raptors.jpg", 200, 200, False)
        raptors.set_from_pixbuf(pixbuf)
        cell_four = Cell("Raptors", raptors)

        spurs = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Spurs.png", 200, 200, False)
        spurs.set_from_pixbuf(pixbuf)
        cell_five = Cell("Spurs", spurs)

        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)