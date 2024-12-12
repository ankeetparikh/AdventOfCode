from collections import defaultdict
with open('../inputs/day12input.txt') as f:
  contents = f.read()

a = contents.split("\n")
n, m = len(a), len(a[0])

f = [[(i, j) for j in range(m)] for i in range(n)]

def find(i, j):
  t = f[i][j]
  if t == (i, j): return t
  f[i][j] = find(t[0], t[1])
  return f[i][j]

def merge(i, j, ni, nj):
  t = find(i, j)
  u = find(ni, nj)
  if t != u:
    f[t[0]][t[1]] = u

for i in range(n):
  for j in range(m):
    c = a[i][j]
    if i + 1 < n and a[i][j] == a[i + 1][j]: merge(i, j, i + 1, j)
    if j + 1 < m and a[i][j] == a[i][j + 1]: merge(i, j, i, j + 1)

area = defaultdict(int)
peri = defaultdict(int)
sides = defaultdict(int)

for i in range(n):
  for j in range(m):
    area[find(i, j)] += 1
    peri[find(i, j)] += 4
    for (di, dj) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
      ni, nj = i + di, j + dj
      if 0 <= ni < n and 0 <= nj < m and find(i, j) == find(ni, nj):
        peri[find(i, j)] -= 1
    
p1 = sum(area[k] * peri[k] for k in area)
print("Part 1:", p1)

# 1-index part 2 to avoid out-of-bounds checks
def ffind(i, j):
  if i == 0 or j == 0 or i == n + 1 or j == m + 1: return (0, 0)
  return find(i - 1, j - 1)

for i in range(1, n + 1):
  for j in range(1, m + 1):

    # top is side
    if ffind(i - 1, j) != ffind(i, j) and (ffind(i, j - 1) != ffind(i, j) or ffind(i - 1, j - 1) == ffind(i, j - 1)):
      sides[ffind(i, j)] += 1
    # bottom
    if ffind(i + 1, j) != ffind(i, j) and (ffind(i, j - 1) != ffind(i, j) or ffind(i + 1, j - 1) == ffind(i, j - 1)):
      sides[ffind(i, j)] += 1

    # left
    if ffind(i, j - 1) != ffind(i, j) and (ffind(i - 1, j) != ffind(i, j) or ffind(i - 1, j - 1) == ffind(i - 1, j)):
      sides[ffind(i, j)] += 1
    # right
    if ffind(i, j + 1) != ffind(i, j) and (ffind(i - 1, j) != ffind(i, j) or ffind(i - 1, j + 1) == ffind(i - 1, j)):
      sides[ffind(i, j)] += 1


p2 = sum(area[k] * sides[k] for k in area)
print("Part 2:", p2)
