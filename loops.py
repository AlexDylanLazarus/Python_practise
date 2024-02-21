# number_of_rows=input("enter a number")
# g=0
# while g<=int(number_of_rows):
#   print(g*'🤩')
#   g+=1

#for loop
# number_of_rows=input("enter a number")
# for g in range(int(number_of_rows)+1):
#   print(g*'🤩')

#range(start, end, step)) remember it dont include the last one so for example range(1,3) itll just do 1 2. similar to slice syntax
  
#how many rows you would like 
#shortcut to rename variable everywhere F2. or right click on it. ctrl +D is for multicursor

# for curr in range(1,50,2):
#   print(curr) 50 doesn't get printed

#task
# player_stats=[10,30,60]
# powered_up_stats=player_stats.copy()
# for i in range(len(player_stats)): 
#   powered_up_stats[i]*=2
  
# print(player_stats,powered_up_stats)

#ORRRRR
# #player_stats=[10,30,60]
# powered_up_stats=[stat * 2 for stat in player_stats]
# print[powered_up_stats]

# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]



# for char in avengers:
#   print(len(char))

# #Task 2
# avengers = [
#   "Hulk",
#   "Iron man",
#   "Black widow",
#   "Captain america",
#   "Spider man",
#   "Thor",
# ]

# for char in avengers:
#   if(len(char) > 10):
#    print(char)

# for curr in range(3):
#   print(curr)


# avengers = [
#   "Hulk",
#   "Iron man",
#   "Black widow",
#   "Captain america",
#   "Spider man",
#   "Thor",
# ]

# for idx in range(len(avengers)):
#   print(avengers[idx])

#ORRR
# filtered_names=[]

# for avenger in avengers:
#   if(len(avenger)>10):
#     print(avenger)
#     filtered_names.append(avenger)
# print(filtered_names)

#ORRR
#I want the avenger from avengers list where the len>10
# filtered_names=[avenger.upper() for avenger in avengers if len(avenger)>10]
# print(filtered_names)
