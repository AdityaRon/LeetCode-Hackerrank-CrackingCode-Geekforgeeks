import re
s, regex = input().strip(), re.compile(r'(\w)(\1)')
match = regex.search(s)
while match:    
    s = s.replace(match.group(),'')
    match = regex.search(s)
print (s if s else 'Empty String')
