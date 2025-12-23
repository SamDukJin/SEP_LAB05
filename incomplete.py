#abstract class
class Transportation(object):
    def __init__(self, start, end, dist):
        if self.__class__ == Transportation:
            raise NotImplementedError
        self.start = start
        self.end = end
        self.distance = dist

    def find_cost(self):
        raise NotImplementedError

#transportation
class Walk(Transportation):
    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, dist)

    def find_cost(self):
        return 0


class Taxi(Transportation):
    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, dist)

    def find_cost(self):
        return self.distance * 40


class Train(Transportation):
    def __init__(self, start, end, dist, stations):
        Transportation.__init__(self, start, end, dist)
        self.stations = stations

    def find_cost(self):
        return self.stations * 5


# main program
travel_cost = 0

trip = [
    Walk("KMITL", "KMITL SCB Bank", 0.6),
    Taxi("KMITL SCB Bank", "Ladkrabang Station", 5),
    Train("Ladkrabang Station", "Payathai Station", 40, 6),
    Taxi("Payathai Station", "The British Council", 3)
]

for travel in trip:
    travel_cost += travel.find_cost()

print(travel_cost)
