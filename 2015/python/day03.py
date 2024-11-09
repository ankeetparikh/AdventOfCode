def locations(input):
  x, y = 0, 0
  s = set()
  s.add((x, y))
  for c in input:
    if c == '>': x += 1;
    if c == '<': x -= 1;
    if c == '^': y += 1;
    if c == 'v': y -= 1;
    s.add((x, y))
  return s

def solve(input):
  print("Part 1:", len(locations(input)))
  print("Part 2:", len(locations(input[::2]) | locations(input[1::2])))


# solve(">")
# solve("^>v<")
# solve("^v^v^v^v^v")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day03input.txt']
solve(open(locs[0]).read())