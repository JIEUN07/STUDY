import re

words = ('seven', 'even', 'prevent', 'revenge', 'maven', 
 'eleven', 'amen', 'event')

pattern = re.compile(r'.even') #.even 앞에 뭐있어야함

for word in words:
 if re.match(pattern, word):
    print(f'The {word} matches')