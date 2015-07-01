'''
Design a valet parking system. Requirements of the valet parking system should be:
1. Customer are given a ticket that they can use to redeem to get their vehicle back
2. Parking spots come in three sizes, small, med, large
3. Thee types of vehicles, small, med, large
-a small vehicle can park in a small, medium, and large spot
-a medium vehicle can park in a medium and large spot
-a large vehicle can park in a large spot

'''

'''
- can make an abstract class Spot and then make SmallSpot, MediumSpot, LargeSpot subclasses
- all the customer can do is get a ticket or submit a ticket
- vehicles may not stay at one spot -- they can be moved around
- spot carries location information - including info about which floor
- employees need to be able to look up the location of a spot

'''

class SpotSize:
    SMALL, MEDIUM, LARGE = 0, 1, 2

class Spot:
    def __init__(self, size, location):
        self.size
        self.location

class ParkingLot:
    def __init__(self, sizes):
        # ex: sizes = [4, 5, 6]
        self.sizes = [4, 5, 6]
        self.occupied = [0, 0, 0]
        self.spots = [] # 2-d array of spots?
        self.table = {} # for doing some lookups

    def issue_ticket(self, car_size):
        spot = self.find_free_spot(car_size)
        # do stuff
        return ticket

    def retrieve_vehicle(self, ticket):
        spot = self.retrieve_vehicle_spot(ticket)
        # do stuff
        return

    def retrieve_vehicle_spot(self, ticket):
        # do stuff
        return spot

    def find_free_spot(self, car_size):
        # do stuff, maybe move stuff around
        return spot

#================================================================================

class CarSize:
    SMALL, MEDIUM, LARGE = 0, 1, 2

class ParkingLot:

    REMAIN_COUNT = [4, 5, 4]

    table = {}

    def issue_ticket(self, car_size):
        # return a string if can find spot, None otherwise

        ticket = None
        spot_size = car_size
        while spot_size <= CarSize.LARGE:
            if self.REMAIN_COUNT[spot_size] > 0:
                ticket = generate_guid()
                while ticket in table:
                    ticket = generate_guid()
                self.REMAIN_COUNT[spot_size] -= 1
                break

        table[ticket] = (car_size, spot_size)
        return ticket

    def retrieve_vehicle(self, ticket):
        if ticket not in table:
            return

        car_size, spot_size = table[ticket]
        self.REMAIN_COUNT[spot_size] -= 1
        del table[ticket]

