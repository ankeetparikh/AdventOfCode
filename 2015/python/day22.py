def solve(input):
  boss = {u[0]:int(u[1]) for x in input.strip().split("\n") if (u:= x.split(": "))}
  print(boss)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day22input.txt']
solve(open(locs[0]).read())