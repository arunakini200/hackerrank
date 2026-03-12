import re

S = input()
k = input()

pattern = re.compile(f'(?={k})')
matches = list(pattern.finditer(S))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1)) 
else:
    print((-1, -1))
