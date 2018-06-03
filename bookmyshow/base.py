from bookmyshow.requester import Requester


class Base(object):
    def __init__(self):
        self.requester = Requester()
