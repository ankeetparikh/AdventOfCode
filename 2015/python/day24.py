import itertools

def solve1(input):
  a = [int(x) for x in input.strip().split("\n")]
  W = sum(a)
  p1 = 10**20
  for sz in range(1, len(a) + 1):
    found = False
    for gr in itertools.combinations(a, sz):
      if sum(gr) * 3 == W:
        pr = 1
        for x in gr: pr *= x
        p1 = min(p1, pr)
        found = True
    if found: break
  
  print("Part 1:", p1)

def solve2(input):
  a = [int(x) for x in input.strip().split("\n")]
  W = sum(a)
  p1 = 10**20
  for sz in range(1, len(a) + 1):
    found = False
    for gr in itertools.combinations(a, sz):
      if sum(gr) * 4 == W:
        pr = 1
        for x in gr: pr *= x
        p1 = min(p1, pr)
        found = True
    if found: break
  
  print("Part 2:", p1)

def solve(input):
  solve1(input)
  solve2(input)

solve("""
1
2
3
4
5
7
8
9
10
11
""")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day24input.txt']
solve(open(locs[0]).read())