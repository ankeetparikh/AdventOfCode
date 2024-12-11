from collections import defaultdict
with open('../inputs/day08input.txt') as f:
  contents = f.read()

a = contents.split("\n")
n = len(a)
m = len(a[0])

z = defaultdict(list)

for i in range(n):
  for j in range(m):
    if a[i][j] == '.': continue
    z[a[i][j]] += [(i, j)]

ant = set()
for k, vec in z.items():
  for i, j in vec:
    for ii, jj in vec:
      if (i, j) == (ii, jj): continue
      di = ii - i
      dj = jj - j
      ni = i + 2 * di
      nj = j + 2 * dj
      if 0 <= ni < n and 0 <= nj < m:
        ant.add((ni, nj))

print("Part 1:", len(ant))

ant = set()
for k, vec in z.items():
  for i, j in vec:
    for ii, jj in vec:
      if (i, j) == (ii, jj): continue
      di = ii - i
      dj = jj - j
      t = 1
      while True:
        ni = i + t * di
        nj = j + t * dj
        if 0 <= ni < n and 0 <= nj < m: 
          ant.add((ni, nj))
          t += 1
        else:
          break

print("Part 2:", len(ant))