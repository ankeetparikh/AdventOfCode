def solve(input):
  a = [int(x) for x in input.strip().split("\n")]
  
  p1, p2 = 0, 0
  for x in a:
    p1 += x // 3 - 2
    y = x
    while y > 0:
      y = y // 3 - 2
      p2 += max(0, y)

  print("Part 1:", p1)
  print("Part 2:", p2)

# solve("100756")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day01input.txt']
solve(open(locs[0]).read())
