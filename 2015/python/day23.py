def solve(input):
  a = input.strip().split("\n")
  N = len(a)

  def ex(z):
    i = 0
    while i < N:
      [ins, v, *d] = a[i].replace(",", "").split()
      if ins == "hlf":
        z[v] //= 2
        i += 1
      elif ins == "tpl":
        z[v] *= 3
        i += 1
      elif ins == "inc":
        z[v] += 1
        i += 1
      elif ins == "jmp":
        i += int(v)
      elif ins == "jie":
        if z[v] % 2 == 0: i += int(d[0])
        else: i += 1
      elif ins == "jio":
        if z[v] == 1: i += int(d[0])
        else: i += 1
    return z
  print("Part 1:", ex({'a': 0, 'b': 0})['b'])
  print("Part 2:", ex({'a': 1, 'b': 0})['b'])

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day23input.txt']
solve(open(locs[0]).read())