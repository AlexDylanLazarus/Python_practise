
participants = [
    {"name": "alex", "email": "alex@gmail.com", "meal_preference":"non_vegetarian", "accomodation":True},
   {"name": "dhara", "email": "dhara@gmail.com", "meal_preference":"vegetarian", "accomodation":False},
   {"name": "quinlan", "email": "quinlan@gmail.com", "meal_preference":"non_vegetarian", "accomodation":True},
   {"name": "thato", "email": "thato@gmail.com", "meal_preference":"non_vegetarian", "accomodation":False}
]

def add_participants(participants, name, email, meal_preference="non_vegetarian", accomodation=False):
  participants.append(
    {"name": name, "email": email, "meal_preference": meal_preference, "accomodation":True})
  return participants

print(add_participants("caleb", "caleb@gmail.com", "vegetarian", True)) 

print(participants)
  