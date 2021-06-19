from collections import deque

n, max_p = int(input()), 15
G = [[] for _ in range(n)]
D, parent = [-1] * n, [[-1]*max_p for _ in range(n)]

for i in range(n-1):
  a, b = map(int,input().split()); a-=1; b-=1
  G[a].append(b)
  G[b].append(a)

# 1. DFS
q = deque([0])
D[0] = 0
while q:
  x = q.popleft()
  for nx in G[x]:
    if D[nx] == -1:
      D[nx] = D[x] + 1
      parent[nx][0] = x
      q.append(nx)

# 2. Preprocess for LCA
for j in range(max_p - 1):
  for i in range(1,n):
    if parent[i][j] != -1:
      parent[i][j+1] = parent[parent[i][j]][j]

# 3. LCA
ans, x = 0, 0
for _ in range(int(input())):
  y = int(input()); y -= 1
  temp = y
  ans += D[x] + D[y]
  if D[x] < D[y]: x, y = y, x
  diff = D[x] - D[y]
  j = 0
  while diff:
    if diff % 2: x = parent[x][j]
    diff //= 2
    j += 1
  if x!=y:
    for j in range(max_p - 1, -1, -1):
      if parent[x][j] != - 1 and parent[x][j] != parent[y][j]:
        x, y = parent[x][j], parent[y][j]
    x = parent[x][j]
  ans -= 2 * D[x]
  x = temp
print(ans)