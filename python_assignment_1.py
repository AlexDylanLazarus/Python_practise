rooms = [
    {"rooms": 1, "bed_type": "Double", "smoking":False, "availability":True},
   {"rooms": 2, "bed_type": "Single", "smoking":True, "availability":False},
   {"rooms": 3, "bed_type": "Single", "smoking":False, "availability":True},
   {"rooms": 4, "bed_type": "Double", "smoking":True, "availability":False},
]

def add_room(rooms, room_number, bed_type="Double", smoking=False):
  rooms.append(
    {"rooms": room_number, "bed_type": bed_type, "smoking": smoking, "availability":True})
  return rooms

print(add_room(rooms, 5, "Single", True))

def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  for room in rooms:
    if(room["bed_type"]==preferred_bed_type and room["smoking"]==smoking_preference) and room["availability"]:
      room["availability"]=False
      return "the room is now booked"
  return "the room is not available for booking, try another room"


print(book_room(rooms, "Single", False))

def list_available_rooms(rooms):
  for room in rooms:
    if room["availability"]:
      print(room)

print(list_available_rooms(rooms))