from threading import Thread
from threading import Lock

class EmailSendThread(Thread):

  def __init__(this, email):
    Thread.__init__(this)
    this.email = email


  def run(this):
    this.email.send_email()
