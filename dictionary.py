# Dictionary -> HashMap -> key : Value
# Keys should be unique

# [] -> List
# () -> Tuple
# {} -> Dictionary

# person = {
#   "name" : "Siya Kolisi",
#   "age" : 32,
#   "country" : "South Africa",
#   "sport" : "rugby"
# }
# print(type(person(items))) #returns list of tuples
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

# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]


# name1=input("enter the name of fruit")
# quantity1=int(input("enter the quantity of fruit"))
# price1=float(input("enter the price of fruit"))
# for items in inventory:
#   if items["name"]==name1:
#     items["quantity"]+=quantity1
#     items["price"]=price1
#   elif items["name"]!=name1:
#     inventory.append({"name":name1, "quantity":quantity1, "price":price1})
# print(inventory)

#their answer answer 
# product_name= input("what is the product name?")
# quantity=int(input("What is the quantity?"))
# price=float(input("What is the price?"))
# new_product={"name":product_name, "quantity":quantity, "price":price}

# for item in inventory:
#   if(item["name"]==product_name):
#     item["quantity"]+= quantity
#     item["price"]=price
#     item_found= True
#     break
#     #only when break not happen then to else
# else: #so for loop can also have an else
# #if(item_found==False): #can also say if not item_found:
#   inventory.append(new_product)
  
# print(inventory)

# 5 pillars of coding -> Good Quality 
# 1. Readability # 70% of your life you are reading code
# 2. Maintainability 
# 3. Extendability(how easy is it to add to existing code)
# 4. Testability (testing team will ask you certain things)
# 5. Performance


# guests = [
#   {"name": "Alice", "age": 25, "code": "VIP123"},
#   {"name": "Bob", "age": 17, "code": "VIP123"},
#   {"name": "Charlie", "age": 30, "code": "VIP123"},
#   {"name": "Dave", "age": 22, "code": "GUEST"},
#   {"name": "Eve", "age": 29, "code": "VIP123"}
# ]

# #my answer
# blacklist = ["Dave", "Eve"]
# # who_not=[]
# who_is=[]
# for people in guests:
#   if people["name"] in blacklist or people["age"] < 21 or people["code"] == "GUEST":
#     who_not.append(people["name"])
#   else:
#     who_is.append(people["name"])
# print(who_is)

#their answer
#PASCAL_CASE
# PASS_CODE="VIP123"
# guestlist=[]
# for guest in guests:
#   if(guest['age']>=21 and guest['code']==PASS_CODE and 
#      guest['name'] not in blacklist):
#     guestlist.append(guest["name"])
# print(guestlist)

#list comprehension
# PASS_CODE="VIP123"
# guestlist=[guest["name"] for guest in guests if guest["age"]>=21 and guest["code"]==PASS_CODE and guest["name"] not in blacklist]
# print(guestlist)


#PEP - Python Enhancement Proposal. Current version is 8


person = {
  "name" : "Siya Kolisi",
  "age" : 32,
  "height" : 186,
  "sport" : "rugby",
  "address" : {
    "city" : "Port Elizabeth",
    "country": "South Africa"
  },
  "school":"Grey high school"
}
#print(person['height']) #this will return an error because there is no key. KeyError

#print(person.get('height')) #this is safer because it wont return an error
#print(person.get('height', 175))# this will return 175. When you added the height then you'll get 186 for both 

# print(person.get('address').get('city')) # will return port elizabeth
# # #OR
# # print(person['address']['city'])
# #print(person.get('stat').get('points')) #to aoid nonetype object ha no attribute 'get'
# print(person.get('stat,{}).get(points'))  #give it an empty dict and it will return none/ not an error

#Dictionary comprehension
# nums={x: x ** 2 for x in range(10)}
# print(nums)

# nums={x: x ** 2 for x in range(10) if x % 2 == 0 }
# print(nums)

# nums= [90, 50, 80]
# for num in enumerate(nums):  #this gives the index and the value
#   print(num )

#unpacking example
# nums= [90, 50, 80]
# for idx, num in enumerate(nums):  #this gives the index and the value
#   print(idx, num ) #datatype is a list of tuples

#exercise 
# students= [
#   {"name":"Alex","experience":2},
#   {"name":"Gemma"},
#   {"name":"Rashay","experience":4},
#   {"name":"Thato"}
# ]

# #After 2024 we want their experience to be updated by 1 year
# for student in students:
#   if student.get("experience"):
#     student["experience"]+=1
#   else:
#     student["experience"]=1   
#   if student.get("experience")==1:
#     student["status"]="junior"
#   elif student.get("experience")==5:
#     student["status"]="senior"
#   elif student.get("experience")==3:
#     student["status"]="Mid-level"
# print(students)


# #ORRRR
# #their version
# for employee in employees:
#   if 'experience' in employees:
#     employee['experience']+=1
#   else:
#     employee['experience']=1

# print(employees)

#print(None+1) Will give error saying incompatable data types
# employees= [
#   {"name":"Alex","experience":2},
#   {"name":"Gemma"},
#   {"name":"Rashay","experience":4},
#   {"name":"Thato"}
# ]


# for employee in employees:
#   employee['experience']=employee.get('experience',0) +1 
#   experience=employee['experience']
#   if(experience >=5):
#     employee['status']="senior"
#   elif(experience >=3 and experience <5):
#     employee['status']="Mid-level"
#   else:
#     employee['status']="junior"
# print(employees)

#copy an object
# movie={
#   "name":"Mr Bones",
#   "year":2001
# }

# # movie_copy=movie.copy()

# # #Unpacking operator for list is *
# # #Unpacking operator for dictionary is **
# # movie_copy2={**movie, "rating": 10}
# # movie_copy3={**movie, "rating": 10, "year":2002} #it will give 2002 now as output instead of 2001. If you had a second year: itll use the last one coz you cant have duplicate keys
# # movie_copy4={"rating": 10, "year":2002, **movie}#the name will come at the end
# # print(movie_copy4)

# # #You can combine objects together
# detail={
#   "actor":"Leon Schuster",
#   "Director": "Dzithendo"
# }

# movie_details={**movie, **detail} # this adds the 2 objects. Preferred
#You can also use 
# movie_details=movie|detail #this is the same as above
# print(movie_details)


# price=[1000,1200,400]
# price_copy=[*price] #use one star coz its list. Another way to copy

# price_copy1=[50,40,*price,60]
# print(price_copy, price_copy1)

# #to combine arrays
# t1= [80,90]
# t2= [50, 60]
# t3= [*t1, *t2] or t1+t2
# print(t3)


