def solve(input):
  [L, H] = [int(x) for x in input.strip().split("-")]
  p1, p2 = 0, 0
  for pi in range(L, H + 1):
    p = str(pi)
    if len(p) == 6 and any(x == y for x, y in zip(p, p[1:])) and all(int(x) <= int(y) for x, y in zip(p, p[1:])): p1 += 1
    if len(p) == 6 and any(p[i - 1] == p[i] and (i - 2 < 0 or p[i - 2] != p[i]) and (i + 1 >= len(p) or p[i] != p[i + 1]) for i in range(1, len(p))) \
      and all(int(x) <= int(y) for x, y in zip(p, p[1:])): p2 += 1

  print("Part 1:", p1)
  print("Part 2:", p2)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day04input.txt']
solve(open(locs[0]).read())
