import re
def solve_slow(input):
  g = re.search(r"row (\d+), column (\d+)", input).groups()
  R, C = [int(x) for x in g]

  v = 20151125
  r, c = 1, 1
  while True:
    if r == R and c == C:
      break
    else:
      v = v * 252533 % 33554393
      if r == 1:
        r, c = c + 1, 1
      else:
        r, c = r - 1, c + 1

  print("Part 1:", v)
  print("Part 2: Finished AOC 2015! :)")

def solve_fast(input):
  g = re.search(r"row (\d+), column (\d+)", input).groups()
  R, C = [int(x) for x in g]

  # The first row are the triangular numbers. Get the top-right
  # element in the previous "/" diagonal and add C to it.
  N = (R + C - 2) * (R + C - 1) // 2 + C
  
  p1 = 20151125 * pow(252533, N - 1, 33554393) % 33554393
  print("Part 1:", p1)
  print("Part 2: Finished AOC 2015! :)")  

def solve(input):
  # solve_slow(input)
  solve_fast(input)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day25input.txt']
solve(open(locs[0]).read())