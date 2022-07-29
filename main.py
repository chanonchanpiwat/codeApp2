from Hotel import Hotel
from Person import Person

def main():
    with open('input.txt','r') as rf:
        with open('output_result.txt','w') as wf:
            for i,line in enumerate(rf):
                line = line.strip('\n').split(' ')
                command = line[0]
                params = line[1:]
                if command == 'create_hotel':
                    floors = int(params[0])
                    roomPerFloor = int(params[1])
                    hotel = Hotel(floors,roomPerFloor)
                    res =  f'Hotel created with {floors} floor(s), {roomPerFloor} room(s) per floor.'
                elif command == 'book':
                    roomNumber = params[0]
                    person = Person(params[1],params[2])
                    res = hotel.book(roomNumber,person)
                elif command == 'checkout':
                    keyID = int(params[0])
                    name = params[1]
                    res= hotel.checkOut(keyID,name)
                elif command == 'checkout_guest_by_floor':
                    floor = params[0]
                    res = hotel.checkout_guest_by_floor(floor)
                elif command == 'list_available_rooms':
                    res = hotel.list_available_rooms()
                elif command == 'get_guest_in_room':
                    roomNumber = params[0]
                    res = hotel.get_guest_in_room(roomNumber)
                elif command == 'list_guest':
                    res = hotel.list_guest()
                elif command == 'list_guest_by_age':
                    maxAge = params[1]
                    res = hotel.list_guest_by_age(maxAge)
                elif command == 'list_guest_by_floor':
                    floor = params[0]
                    res = hotel.list_guest_by_floor(floor)
                elif command == 'book_by_floor':
                    floor = params[0]
                    name = params[1]
                    age = params[2]
                    person = Person(name,age)
                    res = hotel.book_by_floor(floor,person)
                print(res)
                wf.write(res+'\n')

if __name__ == "__main__":
    main()