import functools
import itertools

with open('../inputs/day05input.txt') as f:
  contents = f.read()

rules, updates = contents.split("\n\n")
rules = [list(map(int, r.split("|"))) for r in rules.split("\n")]
updates = [list(map(int, u.split(","))) for u in updates.split("\n")]

c = {**{(x, y): 1 for x, y in rules},**{(y, x): -1 for x, y in rules}}

def good(u):
  return all(c.get((x, y), 0) != -1 for x, y in itertools.combinations(u, 2))

p1, p2 = 0, 0
for u in updates:
  if good(u):
    p1 += u[len(u) // 2]
  else:
    f = sorted(u, key=functools.cmp_to_key(lambda x, y: c[(x, y)]))
    p2 += f[len(f) // 2]

print("Part 1:", p1)
print("Part 2:", p2)