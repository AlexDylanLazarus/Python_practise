# # String, List, Tuple, Dictionary, Sets
# # Sets are like lists but can only have unique values. It is also mutable like lists. 
# # {}
# #No order (No guarantee) when you add

# tech_gadgets= {'smartphone','laptop','smartwatch','tablet','tablet'} #wont return the second tablet
# tech_gadgets_list= ['smartphone','laptop','smartwatch','tablet','tablet']
# print(tech_gadgets)
# print(tech_gadgets_list)

# #add
# tech_gadgets.add('E-reader') #theres no quarantee where itll be added
# tech_gadgets_list.append('E-reader')

# #multiple
# more_gadgets=['Drone','Selfiestick']
# tech_gadgets.update(more_gadgets)
# print(tech_gadgets)

# #Delete
# tech_gadgets.remove('Drone') #dont use remove, use discard
# tech_gadgets.discard('Drone') #if it is not in the set discard wont give an error
# #but remove will 
# tech_gadgets.discard('Gimble')  
# print(tech_gadgets)

# #how to create empty set
# x={}#this is empty dictionary
# empty_set=set() #empty set. Use a set constructor
# print(empty_set)

# outdoor_activities= {'Hiking','Cycling','Swimming'}
# indoor_activities= {'Reading','Gaming','Cycling'}

# #union is for combines them but cycling will only be stated once
# print(indoor_activities.union(outdoor_activities))

# #intersection is for common items
# print(indoor_activities.intersection(outdoor_activities)) #just gives cycling

# print(outdoor_activities.difference(indoor_activities))
# print(indoor_activities.difference(outdoor_activities)) #will give gaming and reading

# print(indoor_activities.symmetric_difference(outdoor_activities)) #gives opposite of intersection

# colors= ["red","blue","red","green","pink","blue"]

# print(set(colors)) #will give unique values #converts it set 

# #"red", "blue", "green", "pink"

# #another way
# x=set()
# print(x.union(colors))

# #or
# y=set()
# for color in colors:
#   y.add(color)
# print(y)

#which are outdoor_gadgets

# outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
# indoor_activities = {'Gaming', 'Reading', 'Cycling'}
# activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

# Task 1
# Which are outdoor_gadgets ? 
# {'Smartwatch',  'Drone'}

# Task 2
# # Which are indoor_gadgets ?

# outdoor_gadgets=set()
# for gadget, activity in activity_gadgets.items():
#   if activity in outdoor_activities:
#     outdoor_gadgets.add(gadget)



# print(outdoor_gadgets)

# # Task 2
# indoor_gadgets=set()
# for gadget, activity in activity_gadgets.items():
#   if activity in indoor_activities:
#     indoor_gadgets.add(gadget)



# print(indoor_gadgets)

# def getGadgetSet(activity_gadgets, activities):
#   gadgets=set()
#   for gadget, activity in activity_gadgets.items():
#     if activity in activities:
#       gadgets.add(gadget)
#   return gadgets
  


# print(getGadgetSet(activity_gadgets, outdoor_activities)) #for set comprehension you dont need to make activity_gadgets into a set 
outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}
def getGadgetSet(activity_gadgets, activities):
  return {gadget for gadget, activity in activity_gadgets.items() if activity in activities}

print(getGadgetSet(activity_gadgets, indoor_activities))

# general flow for comprehension is need loop filter

