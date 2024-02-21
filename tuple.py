#tuple vs list. Tuples are immutable

person=("Alex","SA",20)
print(person,type(person))
#person[0]="Thato" #can't do coz its immutable
#count is for how much occurances of something
print(person.count(20))
print(person.index("SA")) #will return 1
print(person.index("80"))#will give you an error. Find is much better than index.

# tuple dont have remove, pop, append, and insert


