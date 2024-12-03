import math
def solve(input):
  a = input.strip().split("\n")
  N = len(a) # assume square
  locs = []
  for i in range(N):
    for j in range(N):
      if a[i][j] == '#':
        locs.append((i, j))
  
  def red(x, y):
    g = math.gcd(x, y)
    if g == 0: g = 1
    return x / g, y / g

  p1 = 0
  for x, y in locs:
    p1 = max(p1, len(set(red(x - u, y - v) for u, v in locs)) - 1)
  print("Part 1:", p1)


import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day10input.txt']
solve(open(locs[0]).read())
