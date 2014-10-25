#!/usr/bin/env python3

from gi.repository import Gtk, GObject
from easymail_lib import Email
from easymail_lib import Filepath
from easymail_lib import EmailSendThread
from easymail_lib import JSON
#from AccountCreate import CreateAccount


class Handler(object):

  def __init__(this, application):
    this.application = application

  def on_btn_cancel_clicked(this, *args):
    Gtk.main_quit(*args)

  def on_btn_Send_clicked(this, *args):
    print(this.application.email)
    this.application.email.set_to_address(this.application.email_to.get_text())
    this.application.email.set_from_address("padalia.rushabh@gmail.com")

    this.application.email.set_email_subject(this.application.email_subject.get_text())
    this.application.email.set_email_server("smtp.gmail.com:587")
    this.application.email.set_username_and_password("padalia.rushabh@gmail.com" , "Creatives@321.com")

    text_buffer = this.application.email_body.get_buffer()
    this.application.email.set_email_body(text_buffer.get_text(text_buffer.get_start_iter() ,text_buffer.get_end_iter(), True))

    if this.application.store is not None:
      this.application.email.set_attachment_path(this.application.store)

    Ethread = EmailSendThread.EmailSendThread(this.application.email)
    Ethread.setName('SendEmailThread')

    Ethread.start()
    #Ethread.join()
    #this.application.email.send_email()
    print("Mail Send")

  def gtk_main_quit(this, *args):
    Gtk.main_quit(*args)

  def on_btn_create_clicked(this, *args):
    print("button")
    file = "/home/rushabh/Rushabh/EasyMail/src/config/EasyMail.json"
    json = JSON.JSON(file)
    json_data = json.read_json_from_file()
    json.set_json_data(json_data)
    json.convert_to_json(this.application.txt_account_name.get_text(),
                          this.application.txt_password.get_text(),
                          this.application.txt_email.get_text(),
                          "gmail.com",
                          this.application.txt_server.get_text(),
                          this.application.check_default.get_active())
    json.write_json_to_file()

  def on_check_default_toggled(this, checkbox):

    if checkbox.get_active() is False:
      this.default_pressed = True
    else:
      this.default_pressed = False


  def on_menu_create_account_activate(this, *args):
    #create_account = CreateAccount(this.application.builder)
    this.application.window_account_create.show_all()

class EasyMailApplication(Gtk.Application):
  def __init__(this):
    this.setWidgets()
    this.initEmail()
    this.setAttachmentPath()
    this.setWidgets_accountCreate()

  def setWidgets(this):
    this.builder = Gtk.Builder()
    this.builder.add_from_file("/home/rushabh/Rushabh/EasyMail/UI/EasyEmail_Prototype_1.glade")
    this.builder.connect_signals(Handler(this))
    this.window = this.builder.get_object("window_easymail")
    this.window.show_all()

    #Email TextBox
    this.email_to = this.builder.get_object("txt_email_to")
    this.email_subject = this.builder.get_object("txt_email_subject")
    this.email_body = this.builder.get_object("txt_email_body")

    #Treeview
    this.view = this.builder.get_object("attachment_view")
    this.store = this.builder.get_object("liststore")
    this.col = this.builder.get_object("treeviewcolumn")
    this.cell = this.builder.get_object("cellrenderertext")

    #Progressbar
    this.parogressbar = this.builder.get_object("progressbar")


    #statusbar
    this.statusbar = this.builder.get_object("statusbar")


  def setWidgets_accountCreate(this):
    this.window_account_create = this.builder.get_object("window_create_account")
    #this.window.show_all()

    #Email TextBox
    this.txt_account_name = this.builder.get_object("txt_account_name")
    this.txt_email = this.builder.get_object("txt_email")
    this.txt_password = this.builder.get_object("txt_password")
    this.txt_server = this.builder.get_object("txt_server")

    #Default CheckBox
    this.check_default = this.builder.get_object("check_default")
    this.check_default.set_active(False)
    this.default_pressed = this.check_default.get_active()

    #statusbar
    this.statusbar_account_create = this.builder.get_object("statusbar_account_creation")

  def initEmail(this):
    #init Email Object
    this.email = Email.EasyMail()

  def setAttachmentPath(this):
    #get hilighted file path
    this.filepath = Filepath.FilePath()
    this.path = this.filepath.getSelectedFilepath()
    this.setAttachmentPathToTree()

  def setAttachmentPathToTree(this):
    if this.path is not None:
      #append the file array to liststore
      for i in range(len(this.path)):
        this.store.append(this.path[i])

GObject.threads_init()
EasyMail = EasyMailApplication()

Gtk.main()
