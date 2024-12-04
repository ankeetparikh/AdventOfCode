with open('../inputs/day04input.txt') as f:
  contents = f.read()

a = contents.split("\n")
n = len(a)
m = len(a[0])
p1 = 0
for i in range(n):
  for j in range(m):
    for dx in [0, 1, -1]:
      for dy in [0, 1, -1]:
        if dx == 0 and dy == 0: continue
        s = ''
        for d in range(4):
          ni = i + dx * d
          nj = j + dy * d
          if 0 <= ni < n and 0 <= nj < m: s += a[ni][nj]
        if s == 'XMAS': 
          p1 += 1
print("Part 1:", p1)


p2 = 0
for i in range(1, n - 1):
  for j in range(1, m - 1):
    if a[i][j] != 'A': continue
    if set([a[i - 1][j - 1], a[i + 1][j + 1]]) == set(['M', 'S']) and \
       set([a[i - 1][j + 1], a[i + 1][j - 1]]) == set(['M', 'S']):
      p2 += 1
print("Part 2:", p2)