from functools import lru_cache

with open('../inputs/day11input.txt') as f:
  contents = f.read()

@lru_cache(maxsize=100000)
def rec(x, mv):
  if mv == 0: return 1
  if x == 0: return rec(1, mv - 1)
  if len(w:=str(x)) % 2 == 0:
    return rec(int(w[0:(len(w) // 2)]), mv - 1) + rec(int(w[len(w) // 2:]), mv - 1)
  return rec(2024 * x, mv - 1)

a = [int(x) for x in contents.split()]
print("Part 1:", sum(rec(x, 25) for x in a))
print("Part 2:", sum(rec(x, 75) for x in a))