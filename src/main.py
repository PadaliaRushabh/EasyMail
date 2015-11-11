#!/usr/bin/env python3

from gi.repository import Gtk, GObject
from easymail_lib import Email
from easymail_lib import Filepath
from easymail_lib import EmailSendThread
from easymail_lib import JSON


class Handler(object):

  def __init__(self, application):
    self.application = application
    self.selection = None

  def on_btn_cancel_clicked(self, *args):
    Gtk.main_quit(*args)

  def on_btn_Send_clicked(self, *args):
    print(self.application.email)
    self.application.email.set_to_address(self.application.email_to.get_text())
    self.application.email.set_from_address("padalia.rushabh@gmail.com")

    self.application.email.set_email_subject(self.application.email_subject.get_text())
    self.application.email.set_email_server("smtp.gmail.com:587")
    self.application.email.set_username_and_password("padalia.rushabh@gmail.com" , "Creatives@321.com")

    text_buffer = self.application.email_body.get_buffer()
    self.application.email.set_email_body(text_buffer.get_text(text_buffer.get_start_iter() ,text_buffer.get_end_iter(), True))

    if self.application.store is not None:
      self.application.email.set_attachment_path(self.application.store)

    Ethread = EmailSendThread.EmailSendThread(self.application.email)
    Ethread.setName('SendEmailThread')

    Ethread.start()
    #Ethread.join()
    #self.application.email.send_email()
    #print("Mail Send")

  def gtk_main_quit(self, *args):
    Gtk.main_quit(*args)

  def on_btn_create_clicked(self, *args):
    file = "/home/rushabh/Rushabh/EasyMail/src/config/EasyMail.json"
    json = JSON.JSON(file)
    json_data = json.read_json_from_file()
    json.set_json_data(json_data)
    json.convert_to_json(self.application.txt_account_name.get_text(),
                          self.application.txt_password.get_text(),
                          self.application.txt_email.get_text(),
                          "gmail.com",
                          self.application.txt_server.get_text(),
                          self.application.check_default.get_active())
    json.write_json_to_file()


  def on_popup_button_add_attachment_clicked(self, *args):
    file_dialog = Gtk.FileChooserDialog("Select Attachment to Send" , None, Gtk.FileChooserAction.OPEN , (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
    Gtk.FileChooser.set_select_multiple(file_dialog , True)
    response  = file_dialog.run()
    if response == Gtk.ResponseType.OK:
      files = file_dialog.get_filenames()
      for file in files:
        f = [file] #convert each to file and then append1
        self.application.store.append(f)

      file_dialog.destroy()

  def on_popup_button_remove_attachment_clicked(self , *args):

    (model, pathlist) = self.selection.get_selected_rows()
    for path in pathlist: #pass path number in path
        tree_iter = model.get_iter(path)

    model.remove(tree_iter)

  def on_treeview_selection_changed(self,selection):
    (model, pathlist) = selection.get_selected_rows()

    if pathlist is None:
      self.selection = None

    self.selection = selection


    for path in pathlist: #pass path number in path
        tree_iter = model.get_iter(path)
        value = model.get_value(tree_iter,0)
        self.selected = value

  def on_attachment_view_button_press_event(self, treeview , event):
      if event.button == 3: # if right click pressed
        if self.selection is not None:
          self.application.menu_add_remove.show_all()
        else:
          self.application.menu_add.show_all()


  def on_check_default_toggled(self, checkbox):

    if checkbox.get_active() is False:
      self.default_pressed = True
    else:
      self.default_pressed = False


  def on_menu_create_account_activate(self, *args):
    #create_account = CreateAccount(self.application.builder)
    #self.application.setWidgets_accountCreate()
    self.application.window_account_create.show_all()

  def on_popup_menu_add_remove_attachment_focus_out_event(self, *args):
    self.application.menu_add_remove.hide()

  def on_popup_menu_add_attachment_focus_out_event(self, *args):
    self.application.menu_add.hide()

  def on_window_create_account_delete_event(self , *args):
      #Email TextBox
      self.application.txt_account_name.set_text("")
      self.application.txt_email.set_text("")
      self.application.txt_password.set_text("")
      self.application.txt_server.set_text("")

      #Default CheckBox
      self.application.check_default.set_active(False)
      self.application.window_account_create.hide()
      return True

class EasyMailApplication(Gtk.Application):
  def __init__(self):
    self.setWidgets()
    self.initEmail()
    self.setAttachmentPath()
    self.setWidgets_accountCreate()
    self.setWidgets_popup()


  def setWidgets(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file("/home/rushabh/Rushabh/EasyMail/UI/EasyEmail_Prototype_1.glade")
    self.builder.connect_signals(Handler(self))
    self.window = self.builder.get_object("window_easymail")
    self.window.show_all()

    #Email TextBox
    self.email_to = self.builder.get_object("stxt_email_to")
    self.email_subject = self.builder.get_object("txt_email_subject")
    self.email_body = self.builder.get_object("txt_email_body")

    #Treeview
    self.view = self.builder.get_object("attachment_view")
    self.store = self.builder.get_object("liststore")
    self.col = self.builder.get_object("treeviewcolumn")
    self.cell = self.builder.get_object("cellrenderertext")

    #Progressbar
    self.parogressbar = self.builder.get_object("progressbar")


    #statusbar
    self.statusbar = self.builder.get_object("statusbar")


  def setWidgets_accountCreate(self):
    self.window_account_create = self.builder.get_object("window_create_account")
    #self.window.show_all()

    #remove attachment button
    self.popup_button_remove_attachment = self.builder.get_object("popup_button_remove_attachment")
    #self.popup_menu_add_attachment = self.builder.get_object("popup_menu_add_attachment")

    #Email TextBox
    self.txt_account_name = self.builder.get_object("txt_account_name")
    self.txt_email = self.builder.get_object("txt_email")
    self.txt_password = self.builder.get_object("txt_password")
    self.txt_server = self.builder.get_object("txt_server")

    #Default CheckBox
    self.check_default = self.builder.get_object("check_default")
    self.check_default.set_active(False)
    self.default_pressed = self.check_default.get_active()

    #statusbar
    self.statusbar_account_create = self.builder.get_object("statusbar_account_creation")

  def setWidgets_popup(self):
    #popup Menu
    self.menu_add_remove = self.builder.get_object("popup_menu_add_remove_attachment")
    self.menu_add = self.builder.get_object("popup_menu_add_attachment")
    #self.filechooser = self.builder.get_object("filechooserdialog")



    #self.menu_add_remove= self.builder.get_object("menu_add_remove_attachments")

  def initEmail(self):
    #init Email Object
    self.email = Email.EasyMail()

  def setAttachmentPath(self):
    #get hilighted file path
    self.filepath = Filepath.FilePath()
    self.path = self.filepath.getSelectedFilepath()
    self.setAttachmentPathToTree()

  def setAttachmentPathToTree(self):
    if self.path is not None:
      #append the file array to liststore
      for i in range(len(self.path)):
        self.store.append(self.path[i])

GObject.threads_init()
EasyMail = EasyMailApplication()

Gtk.main()
