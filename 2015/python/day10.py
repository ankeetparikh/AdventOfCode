import itertools
def solve(input):
  def iterate(s):
    t = ""
    for x, g in itertools.groupby(s):
      t += str(len(list(g))) + str(x) 
    return t

  s = input
  for i in range(40): s = iterate(s)
  print("Part 1:", len(s))

  s = input
  for i in range(50): s = iterate(s)
  print("Part 2:", len(s))


# solve(r"""
# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day10input.txt']
solve(open(locs[0]).read())