class Room:
    def __init__(self,roomNumber,KeyID = None,guest = None,isBooked = False):
        self.roomNumber = roomNumber
        self.KeyID = KeyID
        self.guest = guest
        self.isBooked = isBooked

    def checkIn(self,Person,KeyID):
        assert(self.isBooked == False ), 'This room is booked'
        self.KeyID = KeyID
        self.isBooked = True
        self.guest = Person

    def checkOut(self):
        assert(self.isBooked == True ), 'This room is not booked'
        self.KeyID = None
        self.isBooked = False
        self.guest = None
    
    def __repr__(self):
        return f'Room:{self.roomNumber} Guest:{self.guest} keyID:{self.KeyID}'