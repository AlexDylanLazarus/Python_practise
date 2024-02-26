# from math import pi
from datetime import datetime

# now= datetime.now()
# print(now)
# print(f"The current date is {now: %d-%m-%Y}") #The current date is  23-02-2024
# #OR
# print(f"The current date is {now: %d/%m/%Y}")
# #to have it always formatted
# print(f"The current date is {now: %d/%m/%Y}")

# salary= 420_000
# #python will ignore the _. It is called numeric operators.

# print(salary)  #this is better for DX

# print(f"Dhara's salary is R{salary:,}")
# print(f"Dhara's salary is R{salary:_}") #some countries use underscores. 
# #You can only use commas and underscores. It is used for seperating numbers

# #float formatting
# print(f"the p value is: {round(pi)}") #you cant specify how much decimal points
# print(f"the pi value is {pi:.2f}") #f denotes its a float and will give to 2 decimal places
# print(f"the pi value is {pi:.3f}")

# #text formatting
# name= "Lilitha"
# person="Quinlan"
# print(f"{name:>20}") #this will move the word by 20 spaces
# print(f"{name:<20}:") #this will move the word by 20 spaces
# print(f"{name:^20}:")#this puts it in the center

#padding with stars or hashes etc
# print(f"{person:*>20}:") 
# print(f"{person:#>20}:")
# print(f"{person:^>20}:")
# #The 3 stuff above will result into 
# # *************Quinlan:
# # ############Quinlan:
# # ^^^^^^^^^^^^^Quinlan:

# caleb= 0.925
# print(f"The test results are out and Caleb got {caleb:.2%}") # will give 92.50%


# #formatting exercise

recipe = {
    "name": "Spaghetti Carbonara",
    "servings": 4,
    "ingredients": ["200g spaghetti", "100g pancetta", "2 eggs", "1/2 cup grated Parmesan", "1 clove garlic"]
}

print(f"{recipe['name']:=^33}")
for ingredient in recipe["ingredients"]:
  print(f"- {ingredient}")
print(f"Serves: {recipe['servings']} people")

# Task 1
# ======= Spaghetti Carbonara =======
# - 200g spaghetti
# - 100g pancetta
# - 2 eggs
# - 1/2 cup grated Parmesan
# - 1 clove garlic
# Serves: 4 people

guests = ["Alice", "Bob", "Charlie"]
party_date = datetime(2024, 3, 14)

# Task 2 - Party Invite
# *       Alice       *
# You are invited to the party on March 14, 2024!
# *        Bob        *
# You are invited to the party on March 14, 2024!
# *      Charlie      *
# You are invited to the party on March 14, 2024!

# print(f"*{guests[0]:^20}*")
# print(f"You are invited to the party on {party_date:%B %d, %Y}!")
# print(f"*{guests[1]:^20}*")
# print(f"You are invited to the party on {party_date:%B %d, %Y}!")
# print(f"*{guests[2]:^20}*")
# print(f"You are invited to the party on {party_date:%B %d, %Y}!")

#OR
for guest in guests:
  print(f"* {guest:^20} *")
  print(f"You are invited to the party on {party_date:%B %d, %Y}!") #Capital B will give you march capitalized


#Multi-line string
#You can also use f string
about_me="""
Hi, My name is Caleb
I stay at Cape Town
"""

print(about_me) #this will print it as is. 

