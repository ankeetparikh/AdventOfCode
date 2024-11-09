import re
import itertools
def solve(input):

  cities = set()
  dist = {}

  for line in input.strip().split("\n"):
    [a, b, d] = re.search(r"(\w+) to (\w+) = (\d+)", line).groups()
    cities.add(a)
    cities.add(b)
    dist[(a, b)] = int(d)
    dist[(b, a)] = int(d)
  
  mind, maxd = 10**20, 0
  for perm in itertools.permutations(cities):
    t = sum(dist[(x, y)] for x, y in zip(perm, perm[1:]))
    if t < mind: mind = t
    if t > maxd: maxd = t
  print("Part 1:", mind)
  print("Part 2:", maxd)

# solve(r"""
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day09input.txt']
solve(open(locs[0]).read())