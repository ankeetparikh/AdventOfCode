def solve(input):
  p1, p2 = 0, -1
  p = 0
  for i, x in enumerate(input):
    if x == '(': p += 1 
    else: p -= 1
    if p == -1 and p2 == -1:
      p2 = i + 1
  p1 = p
  print("Part 1:", p1)
  print("Part 2:", p2)

# solve(")")
# solve("()())")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day01input.txt']
solve(open(locs[0]).read())
