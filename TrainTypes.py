class Subway:

    def __init__(self, name, route):
        self.name = name
        self.route = route
        self.price = 2.40

class Bus:

    def __init__(self, name):
        self.name = name
        self.price = 1.70
        
class Station:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        