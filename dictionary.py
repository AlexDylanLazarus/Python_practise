# Dictionary -> HashMap -> key : Value
# Keys should be unique

# [] -> List
# () -> Tuple
# {} -> Dictionary

person = {
  "name" : "Siya Kolisi",
  "age" : 32,
  "country" : "South Africa",
  "sport" : "rugby"
}

#you use the box for index but now for dictionaries you specify the key and not the index

#the following makes the orginal dictionary changed
#

# print(person.keys())
# print(person.values())
# print(person.items()) #this returns items into a tuple. Items is the one you'll use in for loop

# for detail in person.items():
#   print(detail[0]) #returns the keys
#   #print(detail[1]) #returns the values

# #unpack
# for key, value in person.items():
#   print(key, value)

# books = [
#   {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#   {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#   {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#   {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#   {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]


# for book in books:
#   if book["rating"] >= 4.7:
#     print(book["title"])

#list comprehension
# result= [(book["title"]) for book in books if book["rating"] >= 4.7]
# print(result) 

#A-Z order
# result= [(book["title"]) for book in books if book["rating"] >= 4.7]
# result.sort()
# print(result)

#ORRRR
#if you dont want the array mutated
# result= [(book["title"]) for book in books if book["rating"] >= 4.7]
# print(sorted(result))#sorts it and gives copy

inventory = [
  {"name": "Apple", "quantity": 30, "price": 0.50},
  {"name": "Banana", "quantity": 20, "price": 0.20}
]

name1=input("enter the name of fruit")
quantity1=int(input("enter the quantity of fruit"))
price1=float(input("enter the price of fruit"))
for items in inventory:
  if items["name"]==name1:
    items["quantity"]+=quantity1
    items["price"]=price1
  elif items["name"]!=name1:
    inventory.append({"name":name1, "quantity":quantity1, "price":price1})
print(inventory)

