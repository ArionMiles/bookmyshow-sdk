from bookmyshow.modules.Fundamentals.base import BaseList, BaseObject
from collections.abc import Sequence


class Events(BaseList, Sequence):
    def __len__(self):
        return len(self.events)

    def __getitem__(self, index):
        return self.events[index]

    def __init__(self, data, headers, request):
        super().__init__(data, headers, request)
        self.events = []
        self.process_events(data['moviesData']['BookMyShow']['arrEvents'])

    def process_events(self, events):
        for event in events:
            self.events.append(Event(event, self.r))


class Event:
    def __init__(self, event, request):
        self.r = request
        self.__dict__ = event
