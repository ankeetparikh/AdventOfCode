def solve(input):
  a = [int(x) for x in input.strip().split("\n")]
  n = len(a)
  p1 = 0
  p2, minc = 0, n + 1
  for mask in range(1 << n):
    s = 0
    pc = 0
    for i in range(n): 
      if mask >> i & 1: 
        s += a[i]
        pc += 1
    if s == 150: 
      p1 += 1
      if pc < minc:
        p2 = 1
        minc = pc
      elif pc == minc:
        p2 += 1
  print("Part 1:", p1)
  print("Part 2:", p2)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day17input.txt']
solve(open(locs[0]).read())