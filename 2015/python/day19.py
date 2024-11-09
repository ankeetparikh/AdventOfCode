import re
from functools import lru_cache
def solve(input):
  _reps, mo = input.strip().split("\n\n")
  reps = [x.split(" => ") for x in _reps.split("\n")]
  
  mos = set()
  for fro, to in reps:
    for m in re.finditer(fro, mo):
      newmo = mo[:m.start()] + to + mo[m.end():]
      mos.add(newmo)
  print("Part 1:", len(mos))

  # inf = 10**5
  # @lru_cache(maxsize=10**7)
  # def rec(mo):
  #   # print("rec called on", mo)
  #   if mo == 'e': return 0
  #   has_rec = False
  #   best = inf
  #   for fro, to in reps:
  #     for m in re.finditer(to, mo):
  #       has_rec = True
  #       pre = mo[:m.start()] + fro + mo[m.end():]
  #       best = min(best, rec(pre) + 1)
  #   if not has_rec: return inf
  #   return best
  # print("Part 2:", rec(mo))

solve("""
e => H
e => O
H => HO
H => OH
O => HH

HOH
""")

solve("""
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day19input.txt']
solve(open(locs[0]).read())
