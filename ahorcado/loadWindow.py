import gi
import requests, threading, shutil
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GLib
from ahorcado import juegoAhorcado
class LoadWindow(Gtk.Window):
    spinner = Gtk.Spinner()
    label= Gtk.Label("Cargando elementos...")
    box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
    def __init__(self):
        super().__init__(title="")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.spinner.props.active = True
        self.set_position(Gtk.WindowPosition.CENTER)
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False,0)
        self.add(self.box)
        self.launch_load()

    def launch_load(self):
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()

    def load_json(self):
        response = requests.get('https://raw.githubusercontent.com/HectorVara/DI/master/ahorcado/resources/data.json')
        json_list = response.json()
        result = []
        for json_item in json_list:
            fallos = json_item.get("fallos")

            image_url = json_item.get("url_imagen")
            r = requests.get(image_url, stream=True)
            with open("temp.png", "wb") as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file("temp.png")
            result.append({"fallos": fallos, "gtk_image": image})
        GLib.idle_add(self.start_main_window, result)
    def start_main_window(self, loaded_items_list):
        win= juegoAhorcado(loaded_items_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()
        Gtk.main()