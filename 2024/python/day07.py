import re
with open('../inputs/day07input.txt') as f:
  contents = f.read()

def conc(x, y):
  if y == 0: return 10 * x
  yy = y
  while yy > 0:
    yy //= 10
    x *= 10
  return x + y

p1 = 0
p2 = 0
for line in contents.split("\n"):
  lhs, *tail = [int(x) for x in re.split(r"\D+", line)]
  n = len(tail)
  
  isP1 = True # feels hacky but whatever
  def rec(cur, i):
    if cur > lhs: return False
    if i == n: return cur == lhs
    if isP1: return rec(cur * tail[i], i + 1) or rec(cur + tail[i], i + 1)
    else: return rec(cur * tail[i], i + 1) or rec(cur + tail[i], i + 1) or rec(conc(cur, tail[i]), i + 1)
  
  if rec(tail[0], 1): p1 += lhs
  isP1 = False
  if rec(tail[0], 1): p2 += lhs

print("Part 1:", p1)
print("Part 2:", p2)