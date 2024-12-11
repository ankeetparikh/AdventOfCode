from collections import defaultdict
with open('../inputs/day10input.txt') as f:
  contents = f.read()

a = [[int(x) for x in line] for line in contents.split("\n")]
n, m = len(a), len(a[0])
b = [[set() for x in range(m)] for x in range(n)]
c = [[0 for x in range(m)] for x in range(n)]
p1, p2 = 0, 0
for d in range(9, -1, -1):
  for i in range(n):
    for j in range(m):
      if a[i][j] != d: continue
      if d == 9: 
        b[i][j].add((i, j))
        c[i][j] = 1
      else:
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
          ni, nj = i + di, j + dj
          if 0 <= ni < n and 0 <= nj < m and d + 1 == a[ni][nj]:
            b[i][j] |= b[ni][nj]
            c[i][j] += c[ni][nj]
      if d == 0: 
        p1 += len(b[i][j])
        p2 += c[i][j]
print("Part 1:", p1)
print("Part 2:", p2)