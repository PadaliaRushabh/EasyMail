from threading import Thread
from threading import Lock
from easymail_lib import Notification

class EmailSendThread(Thread):

    def __init__(self, email):
        Thread.__init__(self)
        self.email = email


    def run(self):
        self.email.send_email()
        notification = Notification.Notification()
        notification.send("EasyMail", "Your Message is Send")
    
    
    