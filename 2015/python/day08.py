
def solve(input):
  p1 = 0
  for line in input.strip().split("\n"):
    c = len(line.strip())
    mem = 0
    n = len(line)
    i = 1
    while i < n - 1:
      mem += 1
      if line[i] == "\\":
        i += 1
        if line[i] == 'x': i += 3
        else: i += 1
      else:
        i += 1
    p1 += c - mem
  print("Part 1:", p1)

  p2 = 0
  for line in input.strip().split("\n"):
    need = 2
    for c in line:
      if c == "\"": need += 2
      elif c == "\\": need += 2
      else: need += 1
    p2 += need - len(line)
  print("Part 2:", p2)

solve(r"""
""
"abc"
"aaa\"aaa"
"\x27"
""")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day08input.txt']
solve(open(locs[0]).read())