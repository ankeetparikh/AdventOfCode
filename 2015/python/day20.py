import numpy as np
def solve(input):
  m = int(input)
  L = 1 << 20 # lol edited this manually to speed up the computation
  while True:
    a = np.zeros(L + 1, int)
    ans = -1
    for i in range(1, L):
      a[i::i] += 10 * i
      if a[i] >= m: 
        ans = i
        break
    if ans != -1: break
    L *= 2
  print("Part 1:", ans)

  L = 1 << 20 # same here
  while True:
    a = np.zeros(L + 1, int)
    ans = -1
    for i in range(1, L):
      for j in range(50):
        if i * j < L: a[i * j] += 11 * i
      if a[i] >= m: 
        ans = i
        break
    if ans != -1: break
    L *= 2
  print("Part 2:", ans)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day20input.txt']
solve(open(locs[0]).read())