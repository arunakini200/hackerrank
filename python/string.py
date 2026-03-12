from itertools import groupby
S = input().strip()
result = []
for k, g in groupby(S):
    count = len(list(g))
    result.append((count, int(k)))
print(*result)
