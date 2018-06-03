from bookmyshow.base import Base
from bookmyshow.modules.Quickbook.quickbook import Quickbook


class BookMyShow(Base):
    def __init__(self):
        super().__init__()
        self.quickbook = Quickbook(requester=self.requester)
