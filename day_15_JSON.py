import json
from pprint import pprint

# data = {
#     "employees": [
#         {"name": "Alice", "age": 30, "department": "sales"},
#         {"name": "Bob", "age": 25, "department": "Marketing"},
#     ]
# }

# print(type(data))
# print(data["employees"][0]["age"])

# # convert to jason
# data_json = json.dumps(data, indent=4)

# print(data_json)
# # print(data_json["employees"]) this will give errors because it is now a string

# student = """
#     {
#         'name':'Gemma',
#         'gender':'female'
#     }

# """


# # JSON- Javascript Object Notation - String
# # print(student, student["name"]) also gives error coz it is a string

# sport = {"name": "Dhoni", "dbl": lambda x: x * 2}  # valid dictionary
# # this is valid because u can have a function as a value.
# # functions are treated as first class citizens.
# # functions treated as first class citizens
# # 1. assign a function to variable
# # 2. pass a function as argument
# # 3. Return a function (a function that returns a function))
# #  function being treated as a value

# print(sport["dbl"](10))

# sport_json = json.dumps(sport)
# print(sport_json) #this will give an error because function cant be called in a string
# gives serializing error which means cant convert dictionary because it contains a function

# HOW TO CONVERT BACK FROM JSON TO DICTIONARY
# student_json = """
#         {
#             "name": "gemma",
#             "gender": "female"
#         }
# """
# student1 = json.loads(student_json)
# print(student1)

# bank_data = """
# [
#     {
#         "id": 1,
#         "name": "John Doe",
#         "email": "johndoe@example.com",
#         "isActive": true,
#         "balance": 150.75
#     },
#     {
#         "id": 2,
#         "name": "Jane Smith",
#         "email": "janesmith@example.com",
#         "isActive": false,
#         "balance": 500.50
#     },
#     {
#         "id": 3,
#         "name": "Emily Jones",
#         "email": "emilyjones@example.com",
#         "isActive": true,
#         "balance": 0.00
#     }
# ]
# """

# TASK 1
# bank_data_1 = json.loads(bank_data)


# for user in bank_data_1:
#     if user["isActive"]:
#         user["balance"] *= 1.1


# bank_data_json = json.dumps(bank_data_1, indent=4)


# pprint(bank_data_json)


# TASK 2

# bank_data_1 = json.loads(bank_data)

# bank_data_1 = [
#     (
#         {
#             **user,
#             "balance": user["balance"] * 1.1,
#         }  # get the copy and override the balance
#         if user["isActive"]
#         else 0
#     )
#     for user in bank_data_1
# ]

# bank_data_json = json.dumps(bank_data_1, indent=4)

# pprint(bank_data_json)

# dictionary to string -> dumps
# string to dictionary -> loads


# Every language can understand string
# So json can speak every language because every language uses string
# frontend dont care if it is in python or not, as long as it is in json
# Its called loose coupling(where as long as it is in json)


# tight coupling, is where there is tight dependency.


# why we are using json
# json becomes a universal language
# loose coupling- when you change between different platforms, it dont matter coz all can send json. they are not tightly associated. if u change ur backend, the frontend wont care and vise versa. this means each side is independent
# platform independent- you can send it to any platform as long as it is json.


# Micro service architecture
# python can take long performance wise so add go (80% python and 20% GO). Go will make it faster summarization


# with will not cause errorts

# with open("bank_accounts.json", "w") as file:
#     json.dump(bank_data_1, file, indent=4)


# with open("bank_accounts.json", "r") as file:
#     data = json.load(file)
#     print(data, type(data))


# # Write a file
# with open("bank_accounts.json", "w") as file:
#     json.dump(update_accounts, file, indent=4)


# # Read a file
# with open("bank_accounts.json", "r") as file:
#     data = json.load(file)
#     print(data, type(data))


# Task
# Starting blog_post.json
with open("blog_post.json", "r") as file:
    information = json.load(file)
    # print(information)

posts_summary = []

for post in information["posts"]:
    post_summary = {
        "title": post["title"],
        "author": post["author"],
        "number_of_comments": len(post["comments"]),
    }
    posts_summary.append(post_summary)

summary_data = {"posts_summary": posts_summary}

with open("posts_summary.json", "w") as file:
    json.dump(summary_data, file, indent=4)
