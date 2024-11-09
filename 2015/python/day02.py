def solve(input):
  lines = input.split()
  p1, p2 = 0, 0
  for line in lines:
    a, b, c = sorted([int(x) for x in line.split("x")])
    p1 += 2 * (a * b + a * c + b * c) + a * b
    p2 += 2 * (a + b) + a * b * c
  print("Part 1:", p1)
  print("Part 2:", p2)


# solve("2x3x4")
# solve("1x1x10")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day02input.txt']
solve(open(locs[0]).read())
