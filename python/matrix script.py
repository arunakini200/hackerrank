import re

N, M = map(int, input().split())


matrix = [input() for _ in range(N)]


decoded = ''.join(matrix[i][j] for j in range(M) for i in range(N))

print(re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded))
