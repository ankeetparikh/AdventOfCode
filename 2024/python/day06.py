def part1():
  with open('../inputs/day06input.txt') as f:
    contents = f.read()

  a = contents.split("\n")
  n = len(a)
  m = len(a[0])

  for i in range(n):
    for j in range(n):
      if a[i][j] == '^': si, sj = i, j

  # (-1, 0) -> (0, 1) -> (-1, 0) -> (0, -1) -> (-1, 0)
  def rot_right(di, dj): return (dj, -di)
  def inside(i, j): return 0 <= i < n and 0 <= j < m

  di, dj = -1, 0
  locs = set()

  while True:
    locs.add((si, sj))
    ni, nj = si + di, sj + dj
    if inside(ni, nj):
      if a[ni][nj] == '#':
        di, dj = rot_right(di, dj)
      else:
        si, sj = ni, nj
    else:
      break

  print("Part 1:", len(locs))
  return locs
def part2(locs):
  with open('../inputs/day06input.txt') as f:
    contents = f.read()

  a = contents.split("\n")
  n = len(a)
  m = len(a[0])

  for i in range(n):
    for j in range(m):
      if a[i][j] == '^': si, sj = i, j

  # (-1, 0) -> (0, 1) -> (-1, 0) -> (0, -1) -> (-1, 0)
  def rot_right(di, dj): return (dj, -di)
  def inside(i, j): return 0 <= i < n and 0 <= j < m

  def has_loop(oi, oj):
    # print("has loop called with", oi, oj)
    di, dj = -1, 0
    pi, pj = si, sj
    locs = set()
    while True:
      if (pi, pj, di, dj) in locs: return True
      locs.add((pi, pj, di, dj))
      ni, nj = pi + di, pj + dj
      if inside(ni, nj):
        if a[ni][nj] == '#' or (ni, nj) == (oi, oj):
          di, dj = rot_right(di, dj)
        else:
          pi, pj = ni, nj
      else:
        return False
  p2 = 0
  for i, j in locs: 
    if a[i][j] == '.': # the obstacle must be placed on the guard's path to induce a cycle
      p2 += 1 if has_loop(i, j) else 0
  print("Part 2:", p2)

locs = part1()
part2(locs)