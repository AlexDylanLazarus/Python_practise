#Regex -> Regular expression
import re
# Pattern match in a string

numbers="""
345678, 41234242,65748390, 56478390, 98765444567
"""

# They have 16 digits
# starts with 4

# \d\d\d #anythin 0-9
# \D can be anything other tahn digits
# . means any character
# if you want to atch the full stop then say \.
#[abc] can be a or b or c. Means character set.
# [^abc]s the abc is excluded
# [a-z] anything from a to z
# [A-Z] capital letter 
#[A-Z] \w\w   \w means alphanumerical. it also matches underscore and capital.
#\W #anything other than alphanumerical
#funnn {1,2} copy n 2 times
# if you say n,z it will match the comma also 
#n{2,3} minimum of 2 to 3 
# ^(file_\w+)\.pdf$
# (\w+ (\d+))
# ? to say dont be greedy (.*)x(.*)?
#I love (dogs|cats) works like or
# \s will match space and new line
#\S is the opposite




# quote="To be or not to be"
# # r - raw
# is_be=re.search(r'be$',quote) 
# print(type(is_be)) #this is a type re.match
# output="Present" if is_be else "Not present"
# print(output)


# quote1="funny funy funnnny fuzzy"
# find_be=re.findall(r'fun[nz]{2,}y', quote1) 
# print(find_be)


# text= "This \\ that \\ those"
# matches=re.findall("\\\\", text) #If you dont use r string then you escape it with \\
# matches=re.findall(r"\\", text)
# print(matches)

# tweet="Spoiler: This movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"
# censor_text=re.sub(r'spoiler|beauty',"*" * 7,tweet, flags=re.IGNORECASE)
# print(censor_text)

# list_websites="facebook.com, google.com, twitter.in, amazon.com"
# # result=re.sub(r'(\w+)\.com',"blacklist.com", list_websites)
# result=re.sub(r'(\w+)(\.com)',r' \1.subdomain.\2', list_websites)  #\1 for first capture group \2 for second capture group
# print(result)

names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]
# namey=", ".join(names)
# print(namey)

empty=[re.sub(r'(\w+)\s+(\w+)\s+',r'\2 , \1 ', name) for name in names]
print(empty)

# output = [re.sub(r'\s*(\w+)\s+(\w+)\s*',r'\2, \1', name) for name in names]
# print(output)

# 1. search.  Prints an object. 
# 2. findAll
# 3. sub

#Assignment 
post= "Loving the #sunny weather in #California. #travel #fun"
hash=re.findall(r'#(\w+)',post) 
print(hash)


