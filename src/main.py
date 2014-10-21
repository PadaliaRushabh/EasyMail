#!/usr/bin/env python3

from gi.repository import Gtk
from easymail_lib import Email
from easymail_lib import Filepath


class Handler(object):

  def __init__(this, application):
    this.application = application

  def on_btn_cancel_clicked(this, *args):
    Gtk.main_quit(*args)

  def on_btn_Send_clicked(this, *args):
    this.application.email.set_to_address(this.application.email_to.get_text())
    this.application.email.set_from_address("padalia.rushabh@gmail.com")

    this.application.email.set_email_subject(this.application.email_subject.get_text())
    this.application.email.set_email_server("smtp.gmail.com:587")
    this.application.email.set_username_and_password("padalia.rushabh@gmail.com" , "Creatives@321.com")

    text_buffer = this.application.email_body.get_buffer()
    this.application.email.set_email_body(text_buffer.get_text(text_buffer.get_start_iter() ,text_buffer.get_end_iter(), True))

    if this.application.store is not None:
      this.application.email.set_attachment_path(this.application.store)
    this.application.email.send_email()
    print("Mail Send")

  def gtk_main_quit(this, *args):
    Gtk.main_quit(*args)

class EasyMailApplication(Gtk.Application):
  def __init__(this):
    this.setWidgets()
    this.initEmail()
    this.setAttachmentPath()

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

EasyMail = EasyMailApplication()

Gtk.main()
