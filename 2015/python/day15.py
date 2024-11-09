import re
def solve(input):
  lines = input.strip().split("\n")
  n = len(lines)
  a = []
  for line in lines:
    g = re.search(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line).groups()
    a.append([int(x) for x in g[1:]])

  exact_cal = False
  num_cal = 500
  def rec(i, c):
    if i == n:
      pr = 1
      for k in range(4):
        su = sum(a[j][k] * c[j] for j in range(n))
        if su < 0: su = 0
        pr *= su
      if exact_cal and not sum(a[j][4] * c[j] for j in range(n)) == num_cal: return 0
      return pr
    else:
      rem = 100 - sum(c)
      best = 0
      for j in range(rem if i == n - 1 else 0, rem + 1):
        r = rec(i + 1, c + [j])
        if r > best: best = r
      return best
  print("Part 1:", rec(0, []))
  exact_cal = True
  print("Part 2:", rec(0, []))



# solve(r"""
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day15input.txt']
solve(open(locs[0]).read())