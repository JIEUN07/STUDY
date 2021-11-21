import re

words = ('a gray bird', 'grey hair', 'great look')

pattern = re.compile(r'gr[ea]y')

for word in words:
 if re.search(pattern, word):
    print(f'{word} matches') 

# grey hair matches