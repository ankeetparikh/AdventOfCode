def solve(input):
  def get_pts(path):
    x, y, step = 0, 0, 0
    pts = set((x, y))
    steps = {(x, y): step}
    for ins in path:
      d, k = ins[0], int(ins[1:])
      for i in range(1, k + 1):
        step += 1
        if d == 'R': x += 1
        elif d == 'L': x -= 1
        elif d == 'U': y += 1
        elif d == 'D': y -= 1
        pts.add((x, y))
        if (x, y) not in steps: steps[(x, y)] = step
    return pts, steps

  [a, b] = [x.split(",") for x in input.strip().split("\n")]
  
  ap, ast = get_pts(a)
  bp, bst = get_pts(b)

  inter = ap & bp - set((0, 0))

  p1 = min(abs(x) + abs(y) for (x, y) in inter)
  p2 = min(ast[pt] + bst[pt] for pt in inter)
  
  print("Part 1:", p1)
  print("Part 2:", p2)

# solve("""
# R8,U5,L5,D3
# U7,R6,D4,L4
# """)
  
# solve("""
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83
# """)

# solve("""
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day03input.txt']
solve(open(locs[0]).read())
