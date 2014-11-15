"""
TODO: better security for password and username
      get contacts from different account
      store password in secure way
      get feedback from software if email is successfully devlivered
      get multiple attachment paths
      if a directory contains directory then error appears that directory cannot be opened, solution: convert the directory to zip
"""


#!/usr/bin/env python3

import smtplib
import os
import sys
import mimetypes #for guess mime types of attachment

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.utils import COMMASPACE

class Email(object):
  """
  message = None
  subject = None
  from_address = None
  to_address = None
  body = None
  email_server = None
  attachment = None
"""
  def __init__(self,from_address,to_address,subject,body,email_server,attachment = None):
    self.message = MIMEMultipart()
    self.message['subject'] = subject
    self.message['From'] = from_address
    self.message['TO'] = to_address
    self.body = MIMEText(body, 'plain')
    self.message.attach(self.body)
    self.email_server = email_server

    if attachment is not None:
      self.attachment = attachment
      self.attach_attachment()

  def get_message(self):
    return self.message

  def send_message(self,auth):
    username, password = auth.get_user_auth_details()
    server = smtplib.SMTP(self.email_server)
    server.starttls() #For Encryption
    server.login(username, password)
    server.send_message(self.message)
    server.quit()

  def attach_attachment(self):
    #self.messaege = self.attachment.set_attachment_type(self.message)
    self.attachment.set_attachment_type(self.message)

class Security(object):
  #username = ""
  #password = ""

  def __init__(self,username, password):
    self.username = username
    self.password = password


  def get_user_auth_details(self):
    return self.username, self.password

class Attachment(object):
  #attachment_path = ''

  def __init__(self,attachment_path):
    self.attachment_path = attachment_path

  def is_directory(self, filenamepath):
    return os.path.isdir(filenamepath)

  def is_file(self, filenamepath):
    return os.path.isfile(filenamepath)

  def guess_and_get_attachment_type(self, filenamepath):
    ctype, encoding = mimetypes.guess_type(filenamepath)

    if ctype is None or encoding is not None:
      # No guess could be made, or the file is encoded (compressed), so
      # use a generic bag-of-bits type.
      ctype = "application/octet-stream"

    maintype , subtype = ctype.split('/' , 1)

    if maintype == 'text':
      fp = open(filenamepath)
      attachment = MIMEText(fp.read() , subtype)
      fp.close()
    elif maintype == 'image':
      fp = open(filenamepath , 'rb')
      attachment = MIMEImage(fp.read() , subtype)
      fp.close()
    elif maintype == 'audio':
      fp = open(filenamepath , 'rb')
      attachment = MIMEAudio(fp.read() , subtype)
      fp.close()
    else:
      fp = open(filenamepath , 'rb')
      attachment = MIMEBase(maintype , subtype)
      attachment.set_payload(fp.read()) #Actual message
      fp.close()
      encoders.encode_base64(attachment) # Encode the payload using Base64

    return attachment

  def set_attachment_type(self,message):
    for attachment in self.attachment_path:
      if(self.is_directory(attachment[0])):
        for filename in os.listdir(attachment[0]):
          filenamepath = os.path.join(attachment[0] , filename)
          attachment = self.guess_and_get_attachment_type(filenamepath)
          # Set the filename parameter
          attachment.add_header('Content-Disposition', 'attachment', filename = os.path.basename(filenamepath))
          message.attach(attachment)

      elif(self.is_file(attachment[0])):
        attachmentfile = attachment[0]
        attachment = self.guess_and_get_attachment_type(attachmentfile)
        # Set the filename parameter
        attachment.add_header('Content-Disposition', 'attachment', filename = os.path.basename(attachmentfile))
        message.attach(attachment)
      else:
        print("Unable to open file or directory")

class EasyMail(object):

  def __init__(self):
    self.attachment_path = None

  def set_to_address(self,to_address):
    #self.to_address = COMMASPACE.join(to_address)
    self.to_address = to_address

  def set_from_address(self,from_address):
    self.from_address = from_address

  def set_email_server(self,email_server):
    self.email_server = email_server

  def set_username_and_password(self,username, password):
    self.username = username
    self.password = password

  def set_email_subject(self,subject):
    self.subject = subject

  def set_email_body(self,body):
    self.body = body

  def set_email_body_from_file(self,file):
    fp = open(file ,"r+")
    self.body = fp.read()
    fp.close()

  def set_attachment_path(self,attachment_path):
    self.attachment_path = attachment_path

  def send_email(self):
    auth = Security(self.username , self.password)
    if self.attachment_path is not None:
      attachment = Attachment(self.attachment_path)
      email = Email(self.from_address ,  self.to_address ,  self.subject ,   self.body ,self.email_server ,attachment)
    else:
      email = Email(self.from_address ,  self.to_address ,  self.subject ,   self.body ,email_server = self.email_server )
    email.send_message(auth)


def main():
  mail = EasyMail()
  to = "padalia.rushabh@gmail.com, padalia.rushabh@outlook.com, u5635863@anu.edu.au"
  #to = "padalia.rushabh@gmail.com,padalia.rushabh@outlook.com,u5635863@anu.edu.au"
  #to = ["sshubhadeep@gmail.com" , "gurmeetroks@gmail.com"]
  mail.set_to_address(to)
  mail.set_from_address("padalia.rushabh@gmail.com")
  mail.set_email_server("smtp.gmail.com:587")
  mail.set_username_and_password("padalia.rushabh@gmail.com" , "Creatives@321.com")
  mail.set_email_subject("Hi better looking Python Generated Subject")
  mail.set_email_body("This email is entirely python generated")
  attachment=[["/home/rushabh/Rushabh/EasyMail/Test/d/assignment.pdf"] , ["/home/rushabh/Rushabh/EasyMail/Test/d/gmailScript.py"]]
  mail.set_attachment_path(attachment)
  mail.send_email()

if __name__ == '__main__':
  main()
