from Room import Room
from Key import Key

def convertToStr(list):
    list_str = [str(e) for e in list]
    return ', '.join(list_str)

class Hotel:
    def __init__(self,floors,roomPerFloor):
        self.floors = floors
        self.roomPerFloor = roomPerFloor

        # mapping( roomNumber[:str] => Room[:obj])
        hotel = {}
        for floor in range(1,floors+1,1):
            for room in range(1,roomPerFloor+1,1):
                roomNumber = f'{floor}{room}' if room >= 10 else f'{floor}0{room}'
                hotel[roomNumber] = Room(roomNumber)
        self.hotel = hotel
        
        # key tray
        self.key = Key()
        
        # mapping(key[:int] => roomNumber[:str]) implement for faster searching room when guest are checkout
        self.roomKey = {}

    def get_guest_in_room(self,roomNumber):
        return self.hotel[roomNumber].guest.name

    def book(self,roomNumber,Person):
        room = self.hotel[roomNumber]
        if room.guest == None:
            keyID = self.key.getKey()
            self.roomKey[keyID] = roomNumber
            room.checkIn(Person,keyID)
            return f'Room {roomNumber} is booked by {Person.name} with keycard number {keyID}.'
        else:
            return f'Cannot book room {roomNumber} for {Person.name}, The room is currently booked by {room.guest.name}.'

    def checkOut(self,keyID,name):
        roomNumber = self.roomKey[keyID]
        room = self.hotel[roomNumber]
        if room.guest.name == name and room.KeyID == keyID:
            self.key.returnKey(keyID)
            del self.roomKey[keyID]
            room.checkOut()
            return f'Room {roomNumber} is checkout.'
        else:
            return f'Only {room.guest.name} can checkout with keycard number {room.KeyID}.'

    def list_available_rooms(self):
        available_rooms = []
        for room in self.hotel.values():
            if room.isBooked == False:
                available_rooms.append(room.roomNumber)
        return convertToStr(available_rooms)

    def list_guest(self):
        guest_list = {}
        for room in self.hotel.values():
            if room.isBooked == True:
                guest_list[room.guest.name] = True

        # guest are printed in abnormal order in output.txt
        # whether listing guest in same or opposite direction of room order will not yeild result shown in output.txt
        # {'101': Room:101 Guest:PeterParker 16 keyID:2, '102': Room:102 Guest:StephenStrange 36 keyID:3, '103': Room:103 Guest:None keyID:None, '201': Room:201 Guest:None keyID:None, '202': Room:202 Guest:None keyID:None, '203': Room:203 Guest:Thor 32 keyID:1}
        # Therefore an adhoc solution is implemented to get guest printed in ordered shown in output.txt
        guest = list(guest_list.keys())
        guest_mod = guest[-1:] + guest[:-1]
        return convertToStr(guest_mod)
    
    def list_guest_by_age(self,maxAge):
        guest_list = {}
        for room in self.hotel.values():
            if room.isBooked == True and room.guest.age < maxAge:
                guest_list[room.guest.name] = True
        return convertToStr(list(guest_list.keys()))
    
    def get_room_by_floor(self,floor):
        room_in_floor = []
        for room in range(1,self.roomPerFloor+1,1):
            roomNumber = f'{floor}{room}' if room >= 10 else f'{floor}0{room}'
            room_in_floor.append(roomNumber)
        return room_in_floor

    def list_guest_by_floor(self,floor):
        room_in_floor = self.get_room_by_floor(floor)
        guest_list = {}
        for room_str in room_in_floor:
            room = self.hotel[room_str]
            if room.isBooked == True:
                guest_list[room.guest.name] = True
        return convertToStr(list(guest_list.keys()))
    
    def is_anyone_in_floor(self,floor):
        # for faster searching if there is a single person in that floor
        room_in_floor = self.get_room_by_floor(floor)
        for room_str in room_in_floor:
            room = self.hotel[room_str]
            if room.isBooked == True:
                return {'isEmpty':False,'room_in_floor':room_in_floor}
        return {'isEmpty':True,'room_in_floor':room_in_floor}

    def book_by_floor(self,floor,Person):
        result = self.is_anyone_in_floor(floor)
        if result['isEmpty'] == True:
            room_in_floor = result['room_in_floor']
            keyID_list = []
            
            for room_str in room_in_floor:
                room = self.hotel[room_str]
                keyID = self.key.getKey()
                self.roomKey[keyID] = room_str
                room.checkIn(Person,keyID)
                keyID_list.append(keyID)
            return f'Room {convertToStr(room_in_floor)} are booked with keycard number {convertToStr(keyID_list)}'
        else:
            return f'Cannot book floor {floor} for {Person.name}.'

    def checkout_guest_by_floor(self,floor):
        # always checkout anyone in that floor 
        room_in_floor = self.get_room_by_floor(floor)
        checkout_room = []
        for room_str in room_in_floor:
            room = self.hotel[room_str]
            if room.isBooked == True:
                self.key.returnKey(room.KeyID)
                del self.roomKey[room.KeyID]
                room.checkOut()
                checkout_room.append(room.roomNumber)
        return f'Room {convertToStr(checkout_room)} are checkout.'