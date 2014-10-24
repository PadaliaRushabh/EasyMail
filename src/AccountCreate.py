from gi.repository import Gtk, GObject
from easymail_lib import JSON

class Handler(object):

  def __init__(this, create_account):
    this.create_account = create_account
    this.default_pressed = create_account.check_default.get_active()

  def on_btn_cancel_clicked(this, *args):
    Gtk.main_quit(*args)

  def on_btn_create_clicked(this, *args):

    file = "/home/rushabh/Rushabh/EasyMail/src/config/EasyMail.json"
    mode = 'w+'
    json = JSON.JSON(file,mode)
    json.convert_to_json(create_account.account_name.get_text(),
                          create_account.password.get_text(),
                          create_account.email.get_text(),
                          "gmail.com",
                          create_account.server.get_text(),
                          create_account.check_default.get_active())
    json.write_json_to_file()

  def on_check_default_toggled(this, checkbox):

    if checkbox.get_active() is False:
      this.default_pressed = True
    else:
      this.default_pressed = False

  def gtk_main_quit(this, *args):
    Gtk.main_quit(*args)
  def on_btn_Send_clicked(this, *args):
    pass


class CreateAccount(Gtk.Application):

  def __init__(this, builder):
    this.builder = builder
    this.setWidgets()


  def setWidgets(this):
    this.window = this.builder.get_object("window_create_account")
    this.window.show_all()

    #Email TextBox
    this.account_name = this.builder.get_object("txt_account_name")
    this.email = this.builder.get_object("txt_email")
    this.password = this.builder.get_object("txt_password")
    this.server = this.builder.get_object("txt_server")

    #Default CheckBox
    this.check_default = this.builder.get_object("check_default")
    this.check_default.set_active(False)
    this.default_pressed = this.check_default.get_active()

    #statusbar
    this.statusbar = this.builder.get_object("statusbar_account_creation")

    this.builder.connect_signals(Handler(this))


builder = Gtk.Builder()
builder.add_from_file("/home/rushabh/Rushabh/EasyMail/UI/EasyEmail_Prototype_1.glade")
create_account = CreateAccount(builder)
Gtk.main()
