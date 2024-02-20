# msg="Hi, all"
# print(msg.upper())
# print(msg.lower())
# print(msg.title()) #capitalize the first letter of each word
# print(msg.capitalize())#capitalize the beginning

# msg1="-----Dream is not something that you see in sleep, Dream is something that does not let you sleep-----"
# print(msg1.strip('-')) #removes empty space
# print(msg1.lstrip('-'))
# print(msg1.rstrip('-'))
# print(msg1.find('something')) #it gave you the index of the first letter of the first something.

#string_exercise
# message = "    🚨🔍📱🔑secret_code✌️"
# code="SECRET_CODE✌️"

# key_index=message.find('🔑')
# secret_msg= message[(key_index+1):]
# output=secret_msg.upper()
# if(output==code):
#   print("you are an hacker")
# else:
#   print("try again")

#Task 2: 
#No secret is present

# message = "    🚨🔍📱secret_code✌️"
# key_there= message.find('🔑')
# if(key_there==-1):
#   print("no secret is present")

#task 3
# message = "    🚨🔍📱🔑******secret_code✌️((((("
# key_there=message.find('🔑')
# output=message[(key_there+1):].strip('(*').upper()
# print(output)

# #You can continue chaining methods
# message="    "
# print(message.strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip().strip())
#even if it is empty, it is an empty string. 

#"-----abnc*-&**".strip("-*")
#it will result in abnc*-&

#task 4
quote="Dream is not a Dream until you make it a Dream"
print(quote.replace('dream','🛌'))
print(quote) #it does not change the original string.
print(quote.count('dream'))#its case sensitive

print(quote.startswith('Dream'))#checks if string starts with
print(quote.endswith('Dream'))

bage_no="45445"
print(bage_no.isdigit())#will return True if all the characters are digits
print(bage_no.isalpha()) #will return True if all the characters are alphabets

name="ark"
print(name.islower()) #true if all the characters are lower case

print(len(name))