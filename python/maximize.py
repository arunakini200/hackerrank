from itertools import product
k, m = map(int, input().split())
lists = []
for _ in range(k):
    row = list(map(int, input().split()))[1:]
    lists.append(row)
max_s = 0
for combination in product(*lists):
    current_s = sum(x**2 for x in combination) % m
    if current_s > max_s:
        max_s = current_s

print(max_s)
