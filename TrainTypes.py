class Subway:

    def __init__(self, name, stations):
        self.name = name
        self.stations = stations
        self.price = 2.40

class Station:

    def __init__(self, name, type, line):
        self.name = name
        self.type = type
        self.line = line
        