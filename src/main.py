#!/usr/bin/env python3

from gi.repository import Gtk
from easymail_lib import Email
from easymail_lib import Filepath


class Handler(object):
  def on_btn_cancel_clicked(this, *args):
    Gtk.main_quit(*args)

  def on_btn_Send_clicked(this, *args):
    email.set_to_address(email_to.get_text())
    email.set_from_address("padalia.rushabh@gmail.com")

    email.set_email_subject(email_subject.get_text())
    email.set_email_server("smtp.gmail.com:587")
    email.set_username_and_password("padalia.rushabh@gmail.com" , "Creatives@321.com")

    text_buffer = email_body.get_buffer()
    email.set_email_body(text_buffer.get_text(text_buffer.get_start_iter() ,text_buffer.get_end_iter(), True))
    email.send_email()
    print("Mail Send")


builder = Gtk.Builder()
builder.add_from_file("/home/rushabh/Rushabh/EasyMail/UI/EasyEmail_Prototype_1.glade")
builder.connect_signals(Handler())
window = builder.get_object("window_easymail")
window.show_all()

#Email TextBox
email_to = builder.get_object("txt_email_to")
email_subject = builder.get_object("txt_email_subject")
email_body = builder.get_object("txt_email_body")

'''
#Get list and Treeview Widget
attachment_list = builder.get_object("list_attachment")
attachment_view = builder.get_object("attachment_view")

#Define and append to List filepath
listmodel = Gtk.ListStore(str)

#get hilighted file path
#filepath = Filepath.FilePath()
#path = filepath.getSelectedFilepath()

#for p in path:
  #attachment_list = defined_list.append(p)
listmodel.append(["sdsd"])
#attachment_list = defined_list.append(["sdssdsd"])
#the treeview
tree = Gtk.TreeView(model=listmodel)

#print(defined_list[attachm.ent_list][0])

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Attachment", renderer, text=0)
tree.append_column(column)

attachment_view = Gtk.TreeView.set_model(tree)
'''


email = Email.EasyMail()

#get hilighted file path
filepath = Filepath.FilePath()
path = filepath.getSelectedFilepath()


files = ""
for p in path:
  files = p + files
  email_to.set_text(files)


Gtk.main()
