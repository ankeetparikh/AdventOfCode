import numpy as np

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]


def solve1(input):
  z = input.strip().split("\n")
  n = len(z)
  a, b = np.zeros((n, n), bool), np.zeros((n, n), bool)
  for i in range(n): 
    for j in range(n): 
      a[i][j] = z[i][j] == '#'
  for iter in range(100):
    for i in range(n): 
      for j in range(n):
        neigh_on = 0
        for di, dj in zip(dx, dy):
          ii, jj = i + di, j + dj
          if 0 <= ii < n and 0 <= jj < n:
            neigh_on += a[ii][jj]
        if a[i][j]:
          b[i][j] = neigh_on in [2, 3]
        else:
          b[i][j] = neigh_on == 3
    a, b = b, a
  print("Part 1:", np.count_nonzero(a))

def solve2(input):
  z = input.strip().split("\n")
  n = len(z)
  a, b = np.zeros((n, n), bool), np.zeros((n, n), bool)

  corners = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
  for i in range(n): 
    for j in range(n): 
      a[i][j] = z[i][j] == '#' or (i, j) in corners
  for iter in range(100):
    for i in range(n): 
      for j in range(n):
        neigh_on = 0
        for di, dj in zip(dx, dy):
          ii, jj = i + di, j + dj
          if 0 <= ii < n and 0 <= jj < n:
            neigh_on += a[ii][jj]
        if a[i][j]:
          b[i][j] = neigh_on in [2, 3] or (i, j) in corners
        else:
          b[i][j] = neigh_on == 3 or (i, j) in corners
    a, b = b, a
  print("Part 2:", np.count_nonzero(a))

def solve(input):
  solve1(input)
  solve2(input)

# solve("""
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..
# """)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day18input.txt']
solve(open(locs[0]).read())