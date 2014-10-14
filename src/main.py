from gi.repository import Gtk


class Handler(object):
  def on_btn_cancel_clicked(this, *args):
    Gtk.main_quit(*args)

  def on_btn_Send_clicked(this, *args):
    print("Hello")



builder = Gtk.Builder()
builder.add_from_file("../UI/EasyEmail_Prototype_1.glade")
builder.connect_signals(Handler())
window = builder.get_object("window_main")
window.show_all()


Gtk.main()
