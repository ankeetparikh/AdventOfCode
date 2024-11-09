import json
def solve(input):
  ignore_red = False
  def rec(a):
    if type(a) == list:
      return sum(rec(x) for x in a)
    elif type(a) == dict:
      if ignore_red and "red" in a.values(): return 0
      return sum(rec(y) for x, y in a.items())
    elif type(a) == int:
      return a
    else: return 0

  print("Part 1:", rec(json.loads(input)))
  ignore_red = True
  print("Part 2:", rec(json.loads(input)))


# solve('[1, 2, 3]')
# solve('[1,{"c":"red","b":2},3]')

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day12input.txt']
solve(open(locs[0]).read())
