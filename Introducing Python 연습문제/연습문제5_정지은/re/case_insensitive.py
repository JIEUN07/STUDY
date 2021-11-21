import re

words = ('dog', 'Dog', 'DOG', 'Doggy')

pattern = re.compile(r'dog', re.IGNORECASE)

for word in words:
 if re.match(pattern, word):
    print(f'{word} matches')


# dog matches
# Dog matches
# DOG matches
# Doggy matches