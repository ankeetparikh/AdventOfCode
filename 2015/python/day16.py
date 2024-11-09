import re
def solve(input):
  m = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
  }

  p1 = 0
  p2 = 0
  for line_num, line in enumerate(input.strip().split("\n")):
    g = re.search(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line).groups()
    n = len(g)
    
    mm = {}
    for i in range(1, n, 2): mm[g[i]] = int(g[i + 1])

    good = True
    for k, v in mm.items(): 
      if m[k] != v: 
        good = False
    if good: p1 = line_num + 1

    good = True
    for k, v in m.items():
      if k in ["cats", "trees"]:
        if k in mm and mm[k] <= m[k]: good = False
      elif k in ["pomeranians", "goldfish"]:  
        if k in mm and mm[k] >= m[k]: good = False
      else:
        if k in mm and mm[k] != m[k]: good = False
    if good: p2 = line_num + 1


  print("Part 1:", p1)
  print("Part 2:", p2)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day16input.txt']
solve(open(locs[0]).read())