import re
import itertools
def solve(input):

  def get_opt(guests, diff):
    n = len(guests)
    opt = 0
    for perm in itertools.permutations(guests):
      cur = 0
      for i in range(n):
        j = (i + 1) % n
        cur += diff[(perm[i], perm[j])] + diff[(perm[j], perm[i])]
      if cur > opt: opt = cur
    return opt

  diff = {}
  guests = set()
  for line in input.strip().split("\n"):
    [x, d, amt, y] = re.search(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).", line).groups()
    guests.add(x)
    guests.add(y)
    diff[(x, y)] = int(amt) * (-1 if d == 'lose' else 1)
  
  print("Part 1:", get_opt(guests, diff))
  
  for g in guests:
    diff[("me", g)] = diff[(g, "me")] = 0
  guests.add("me")
  print("Part 2:", get_opt(guests, diff))

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day13input.txt']
solve(open(locs[0]).read())
