import itertools
import numpy as np
weapons = [
  ["Dagger",        8,     4,       0,],
  ["Shortsword",   10,     5,       0,],
  ["Warhammer",    25,     6,       0,],
  ["Longsword",    40,     7,       0,],
  ["Greataxe",     74,     8,       0,],
]

armor = [
  ["Leather",      13,     0,       1,],
  ["Chainmail",    31,     0,       2,],
  ["Splintmail",   53,     0,       3,],
  ["Bandedmail",   75,     0,       4,],
  ["Platemail",   102,     0,       5,],
]

rings = [
  ["Damage +1",    25,     1,       0,],
  ["Damage +2",    50,     2,       0,],
  ["Damage +3",   100,     3,       0,],
  ["Defense +1",   20,     0,       1,],
  ["Defense +2",   40,     0,       2,],
  ["Defense +3",   80,     0,       3,],
]

def solve(input):
  boss = {u[0]:int(u[1]) for x in input.strip().split("\n") if (u:= x.split(": ")) }

  p1 = 1000
  p2 = 0

  for W in weapons:
    for Ai in range(len(armor) + 1):
      for x in [()] + list(itertools.combinations(rings, 1)) + list(itertools.combinations(rings, 2)):
        stats = np.array(W[1:], int)
        if Ai < len(armor): stats += np.array(armor[Ai][1:], int)
        for ring in x: stats += np.array(ring[1:], int)

        ph, pd, pa = 100, stats[1], stats[2]
        bh, bd, ba = boss['Hit Points'], boss['Damage'], boss['Armor']

        peff = max(1, pd - ba)
        beff = max(1, bd - pa)
        
        p_need = (bh + peff - 1) // peff
        b_need = (ph + beff - 1) // beff
        
        if p_need <= b_need: p1 = min(p1, stats[0])
        else: p2 = max(p2, stats[0])

  print("Part 1:", p1)
  print("Part 2:", p2)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day21input.txt']
solve(open(locs[0]).read())