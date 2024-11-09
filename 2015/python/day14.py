import re
def solve(input):
  T = 2503
  def distance(sp, go, rest, t):
    per = go + rest
    return sp * (t // per * go + min(t % per, go))
  data = {}
  for line in input.strip().split("\n"):
    [x, *tail] = re.search(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line).groups()
    data[x] = [int(x) for x in tail]
  
  p1 = max(distance(sp, go, rest, T) for sp, go, rest in data.values())
  print("Part 1:", p1)
  
  pts = {x:0 for x in data}
  for i in range(1, T + 1):
    distances = {x:distance(sp, go, rest, i) for x, [sp, go, rest] in data.items()}
    mxd = max(distances.values())
    for x, di in distances.items():
      if di == mxd: pts[x] += 1
  print("Part 2:", max(pts.values()))


import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day14input.txt']
solve(open(locs[0]).read())