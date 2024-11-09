import string
def inc(p):
  q = list(p)
  n = len(q)
  i = n - 1
  while q[i] == 'z':
    q[i] = 'a'
    i -= 1
  q[i] = chr(ord(q[i]) + 1)
  return ''.join(q)
def valid(p):
  if not any(ord(x) + 1 == ord(y) and ord(y) + 1 == ord(z) for x, y, z in zip(p, p[1:], p[2:])): return False
  if any(x in "iol" for x in p): return False
  if sum(1 for x in string.ascii_lowercase if str(x + x) in p) < 2: return False
  return True
def ne(p):
  while True:
    p = inc(p)
    if valid(p):
      return p
def solve(input):
  p1 = ne(input)
  print("Part 1:", p1)
  print("Part 2:", ne(p1))


# solve(r"""

# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day11input.txt']
solve(open(locs[0]).read())