

class Event:

    __slots__ = ('name', '_location', '__id', 'participants')

    def __init__(self, name, location):
        self.name = name
        self._location = location
        self.__id = 1
        self.participants = []

    def __str__(self):
        return f"{self.name} location: {self._location} id {self.__id}"
