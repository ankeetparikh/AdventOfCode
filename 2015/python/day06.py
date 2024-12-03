import numpy as np
import re
def solve(input):
  a = np.zeros((1000, 1000), bool)
  b = np.zeros((1000, 1000), int)

  for line in input.split("\n"):
    g = re.search(r"(\d+),(\d+)\s+through\s+(\d+),(\d+)", line).groups()
    x, y, xx, yy = [int(x) for x in g]
    if line.startswith("toggle"):
      a[x:xx + 1, y:yy + 1] ^= True
      b[x:xx + 1, y:yy + 1] += 2
    elif line.startswith("turn on"):
      a[x:xx + 1, y:yy + 1] = True
      b[x:xx + 1, y:yy + 1] += 1
    else:
      a[x:xx + 1, y:yy + 1] = False
      b[x:xx + 1, y:yy + 1] -= 1
      b[b < 0] = 0

  print("Part 1:", np.count_nonzero(a))
  print("Part 2:", b.sum())


import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day06input.txt']
solve(open(locs[0]).read())