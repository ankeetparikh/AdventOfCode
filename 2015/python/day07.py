from functools import lru_cache
def solve(input):
  
  use_new_b = False
  new_b_val = 0

  @lru_cache
  def get(x):
    if use_new_b and x == 'b': return new_b_val
    if x[0].isdigit(): return int(x)
    for ins in input.strip().split("\n"):
      l, r = ins.split(" -> ")
      if r != x: continue
      if "AND" in l:
        u, v = l.split(" AND "); return get(u) & get(v)
      elif "OR" in l:
        u, v = l.split(" OR "); return get(u) | get(v)
      elif "LSHIFT" in l:
        u, v = l.split(" LSHIFT "); return get(u) << get(v)
      elif "RSHIFT" in l:
        u, v = l.split(" RSHIFT "); return get(u) >> get(v)
      elif "NOT" in l:
        u = l.split("NOT ")[1]; return 65535 ^ get(u)
      else:
        return get(l)
  p1 = get('a')
  print("Part 1:", p1)

  get.cache_clear()
  use_new_b = True
  new_b_val = p1
  print("Part 2:", get('a'))

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day07input.txt']
solve(open(locs[0]).read())