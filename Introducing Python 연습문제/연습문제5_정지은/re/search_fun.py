import re

words = ('book', 'bookworm', 'Bible', 
 'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'book')

for word in words:
 if re.search(pattern, word):  # search 아무데나
    print(f'The {word} matches')