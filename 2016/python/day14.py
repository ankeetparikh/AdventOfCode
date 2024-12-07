from functools import lru_cache
import hashlib

def solve(s):
  @lru_cache(maxsize=10000)
  def nth_md5(n):
    t = s + str(n)
    return hashlib.md5(t.encode("utf-8")).hexdigest()
  
  p1 = 0
  i = 0
  j = -1
  while True:
    

  print("Part 1:", p1)
solve("abc")

# with open('../inputs/day14input.txt') as f:
  # s = f.read()