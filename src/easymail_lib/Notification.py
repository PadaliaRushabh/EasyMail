from gi.repository import Notify

class Notification(object):
    
    def __init__(self):
        Notify.init("Easymail")
        
    def send(self , title , message):
        notification = Notify.Notification.new(title , message)
        notification.show()
        