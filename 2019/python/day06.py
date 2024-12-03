def solve(input):
  lines = input.strip().split("\n")
  p = {}
  for line in lines:
    a, b = line.split(")")
    p[b] = a

  hei = {}
  def rec(x):
    if x in hei: return hei[x]
    hei[x] = 0
    if x in p: hei[x] = 1 + rec(p[x])
    return hei[x]  
  for x in p: rec(x)
  print("Part 1:", sum(hei.values()))

  def dist(x, y):
    u, v = x, y
    if hei[u] > hei[v]: u, v = v, u
    while hei[v] > hei[u]: v = p[v]
    while u != v: u, v = p[u], p[v]
    return hei[x] + hei[y] - 2 * hei[u]

  print("Part 2:", dist(p['YOU'], p['SAN']))

# solve("""
# COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN
# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day06input.txt']
solve(open(locs[0]).read())
