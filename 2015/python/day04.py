import hashlib

def f(input, z):
  i = 0
  while not hashlib.md5((input + str(i)).encode("utf-8")).hexdigest().startswith("0" * z):
    i += 1
  return i

def solve(input):
  print("Part 1:", f(input, 5))
  print("Part 2:", f(input, 6))

# solve("abcdef")
# solve("pqrstuv")

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day04input.txt']
solve(open(locs[0]).read())