import string
def solve(input):
  def p1_f(word):
    vows = sum(1 if x in "aeiou" else 0 for x in word)
    rep = any(str(x + x) in word for x in string.ascii_lowercase)
    bad = any(x in word for x in ["ab", "cd", "pq", "xy"])
    return vows >= 3 and rep and not bad
  def p2_f(word):
    c1 = any(word[i:i + 2] in word[i + 2:] for i in range(len(word) - 2))
    c2 = any(x == y for (x, y) in zip(word, word[2:]))
    return c1 and c2
  
  words = input.split()
  print("Part 1:", sum(1 for w in words if p1_f(w)))
  print("Part 2:", sum(1 for w in words if p2_f(w)))

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day05input.txt']
solve(open(locs[0]).read())