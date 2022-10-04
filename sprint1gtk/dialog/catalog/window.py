import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class MainWindow(Gtk.Window):
    image= Gtk.Image.new_from_file("C:\\msys64\\home\\Hector\\DI\\sprint1gtk\\dialog\\catalog\\data\\edited\\Suns.jpg")
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

        
        cell_one= Cell("Suns", Gtk.Image.new_from_file("C:\\msys64\\home\\Hector\\DI\\sprint1gtk\\dialog\\catalog\\data\\edited\\Suns.jpg"))
        cell_two = Cell("Hornets", Gtk.Image.new_from_file(
            "C:\\msys64\\home\\Hector\\DI\\sprint1gtk\\dialog\\catalog\\data\\edited\\Hornets.png"))
        cell_three = Cell("Nets", Gtk.Image.new_from_file(
            "C:\\msys64\\home\\Hector\\DI\\sprint1gtk\\dialog\\catalog\\data\\edited\\Nets.jpg"))
        cell_four = Cell("Raptors", Gtk.Image.new_from_file(
            "C:\\msys64\\home\\Hector\\DI\\sprint1gtk\\dialog\\catalog\\data\\edited\\Raptors.jpg"))
        cell_five = Cell("Spurs", Gtk.Image.new_from_file(
            "C:\\msys64\\home\\Hector\\DI\\sprint1gtk\\dialog\\catalog\\data\\edited\\Spurs.png"))
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)