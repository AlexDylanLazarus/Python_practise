#Assignment
import re

post= "Loving the #sunny weather in #California. #travel #fun"
hash=re.findall(r'#(\w+)',post) 
print(hash)