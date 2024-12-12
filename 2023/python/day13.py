
def solve1(s):
  s = s.strip().split("\n\n")
  t = 0
  for board in s:
    a = board.split()
    n, m = len(a), len(a[0]) 
    for I in range(n - 1):
      good = True
      for i in range(n):
        for j in range(m):
          r = (I + I - i + 1) if i <= I else (I + 1 - (i - I))
          if 0 <= r < n and a[i][j] != a[r][j]: 
            good = False
            break
      if good:
        t += 100 * (I + 1)
    for J in range(m - 1):
      good = True
      for i in range(n):
        for j in range(m):
          c = (J + J - j + 1) if j <= J else (J + 1 - (j - J))
          if 0 <= c < m and a[i][j] != a[i][c]: 
            good = False
            break
      if good:
        t += (J + 1)
  print(t)

def solve2(s):
  s = s.strip().split("\n\n")
  def refs(a):
    n, m = len(a), len(a[0])
    v, h = [], []
    for I in range(n - 1):
      good = True
      for i in range(n):
        for j in range(m):
          r = (I + I - i + 1) if i <= I else (I + 1 - (i - I))
          if 0 <= r < n and a[i][j] != a[r][j]: 
            good = False
            break
      if good: h += [I]
    for J in range(m - 1):
      good = True
      for i in range(n):
        for j in range(m):
          c = (J + J - j + 1) if j <= J else (J + 1 - (j - J))
          if 0 <= c < m and a[i][j] != a[i][c]: 
            good = False
            break
      if good: v += [J]
    return v, h
  t = 0
  for board in s:
    a = [list(x) for x in board.split()]
    v, h = refs(a)
    n, m = len(a), len(a[0])
    vs = set()
    hs = set()
    for i in range(n):
      for j in range(m):
        tmp = a[i][j]
        a[i][j] = '.' if a[i][j] == '#' else '#'
        vv, hh = refs(a)
        a[i][j] = tmp
        if v != vv and len(vv):
          vs.add(list(set(vv) - set(v))[0])
        if h != hh and len(hh): 
          hs.add(list(set(hh) - set(h))[0])
    t += sum(x + 1 for x in vs)
    t += sum(100 * (x + 1) for x in hs)
  print(t)

def solve(s):
  solve1(s)
  solve2(s)

solve("""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""")

solve("""
#..###..#####
###..#.......
.##.#.#.###..
#####....####
#####....####
.##.#.#.###..
###..#.......
#..###..#####
#.##.##.....#
#########.###
#.##.#..#.###
#.##.#..#.###
#########.###
#.##.##.....#
#.####..#####
###..#.......
.##.#.#.###..

.....#########.
#.#..#...#..#..
.####...#.#.#..
#####...#.#.#..
#.#..#...#..#..
.....#########.
###..#....####.
.#...###..#...#
...#########.#.
##.##.##.#####.
##.##.##.#####.
...#########.#.
.#...###..#...#
###..#....####.
.....#########.
#.#..#...#..#..
#####...#.#.#..

#.####..#####
.##..##...###
...##...#####
##..#.##.....
..##.#.#.####
.##....######
.#...###.####
##.##..#.####
#...##.#.....
...#.###.#..#
#.#...###.##.
....#..#..##.
##.......#..#
.#.##..#.####
.#.##..#.####
##.......#..#
....#..#..##.

####.#.
##.#.##
#..#...
.#.#...
######.
...#.#.
...#.#.
######.
.#.#...
#.##...
##.#.##
####.#.
###..#.
##.###.
.....#.
.....#.
##.###.

....##...
..##....#
...#.#.##
...#.#.##
..##....#
....##...
##...#..#
..#.#..#.
...###..#
##.####.#
..#...#..
.#...###.
...#..#..

.#.######.#....
##.#....#.##..#
#.##.##.##.####
#.#...#..#.####
############..#
...#.##.#......
...#....#......
###.#..#.###..#
..########..##.
.##########....
.#.##..##.#.##.

##..#.#
....##.
##...##
#...###
..#.###
.##..#.
...#.#.
...#.#.
.#...#.
.#...#.
...#.#.
...#.#.
.##..#.

.####..###...
..##.......##
##..##..#.#..
........#####
#.##.####..##
#.##.###.#...
##..##.#.....
#.##.######.#
..##..##.#.##
#....##..#.##
##..##...#...
########.##..
#....####.#..
..##..#..####
######.###.##
######.#.##..
..##...#..###

...##.....#..##
..#..#.....#...
##.##.##.#..#..
..#..#...##..##
..........##...
..#..#..##..#..
#......###.#...
#..##..#..#.###
........#.#....
##....##.#.##..
##.##.###.#..##
##....###.##.##
#.####.#.#..#..
.######...##...
...##..##..#.##
.##..##.#.###..
.#....#.##.##..

.#.##..##.#
..##.##.##.
##..#..#..#
.#..####..#
#..........
..##....##.
..##....##.
##..####..#
.##########
#....##....
..##.##.##.
#..........
#####..####

#....##....
.#....#.#..
..#...#.###
###...###..
....#.#.###
#.#.##.####
..#######..
.##...#.#..
.##...#.#..
..#######..
#.#.##.####
....#.#.###
.##...###..
..#...#.###
.#....#.#..

.#....##..#
#.#..###..#
#.##...#..#
#..#####..#
####.#.#..#
.#.###.#..#
####...#..#
.##.#.#.##.
#....#.####
#.##...#..#
##..####..#
.###..##..#
.#.#..##..#
##..####..#
#.##...#..#

#..##.#.#.#..
#..##.#.#.##.
.##..#.....#.
.##..##......
#####..######
#.###.##...##
...##.#..##..
#.##...#..#.#
...#..###..##
#.#.##..#.#.#
.....#..#####
#.#...#.#...#
#.#...#.#...#
.....#..#####
#.#.##..#.#.#
...#..###..##
#.##...#..#.#

#..#.##..####
####...#.####
.##..#..##..#
.#..#.#.##..#
.###...#.....
#.#.###.#####
#.#.#########

#.##.##.##.##..##
...#....#...#....
.....##.....#.###
#...####...#.#...
..#.####.#..#.#..
#....##....####..
#...#..#...#.####
.#.######.#..#.##
##.#.##.#.#####..
.##......##.#.###
..###..###....###
............##...
###.####.###..###
#..##..##..#.....
.#..#.##..#...#..

.......#..##.##
..##...#.##.#.#
##..##.##.#..#.
##..######...#.
######..######.
..##..#.####..#
#.##.#.#.#..##.
######...##..##
##########...##
##..####.##....
######...##....
..##..####.##.#
..##..###.#.#.#

#####.#.######.
#.##.#####.##.#
...#...#..##.##
.#......#..#.##
.#......#..#.##
...#...#..##.##
#.##.#####.##.#
#####.#.######.
....#.####.####
...####..#.###.
...####.#.#.###
...####.#...###
...####..#.###.

###..####
....###.#
....###.#
#.#.##...
..#.....#
..#.....#
#.#.##...
....###.#
....###.#
###..##.#
....#.#..
##....##.
.#.#.....
.#.#.....
##....##.

....##.
.##....
..##..#
#.#####
##.####
###....
##.....
##.####
#.#####
..##..#
.##....
....##.
.#..##.
#.#....
.#..##.

..#..#....##..#
..#..#......##.
##....##..#...#
.######.##..##.
##....###.##..#
.#.##.#...#....
#.####.#.##....

.#.#...#.#.#..#
...###...##.##.
.##.....#......
.##.....#......
...###...##.##.
.#.#...#.#.#..#
#..##...###.#..
..#.#.#.#..###.
..#.#.#.#..###.
#..##...###.#..
.#.#...#.#.#..#
...###...##.##.
###.....#......

..#..#.#..#
..#..#.#..#
###..##...#
######.#.##
##....#####
..##.#.##..
..##...###.
...#....###
..#.##..#..
##.......##
##..##...#.
##..####.##
##..#.....#
.####..#..#
..##.....#.

##..########...
#....###...#...
.......#.#...##
#....##..#.##.#
#######.#..#.##
..##...##....#.
#.##.#.#.###..#
#.##.##.#.##...
#.##.#.####...#
.#..#..#.#...##
.#..#..#.#...##
#.##.#.####...#
#.##.##.#.##..#

##.##.###.....#
.....###.###.##
...#.#.##..##..
..#.######..#..
...#.#..#.##.##
..#..#.###.....
..##..#....##..

.#.###..##.
.#...#####.
#..##.###.#
..####.#...
#..#...#...
####.##..##
..###......
..###......
####.##..##
#..#...#...
..####.#...
#..##.#.#.#
.#...#####.
.#.###..##.
.#.###..##.

##..##..#####..
#.##.##..#...#.
#....#.##.#..##
##..######..###
..##...##..##..
..##...##..##..
##..######..###
#....#.##.#..##
#.##.##..#...#.
##..##..#####..
....#.##..##.##
#.##.##.##..##.
.#..#.#..##.###

.#..########..#..
#...#......#...##
.#....####....#..
######.##.#######
...##.#..#.##....
#....######.#..##
###....##....####
##.###.##.###.###
##.#..####..#.###
#..##......##..##
#.##...##...##.##
....########.....
.###.##..##.###..
.##..##..##..##..
##...#.##.#...###

..#.##.#....#
##.#..#.####.
.########..##
#.#.##.#.##.#
..######....#
#..#..#..##..
#.#.##.#.##.#
.#..##..#..#.
...#..#......
#...##...##..
#.##..##.##.#
#.######.##.#
##.#..#.###..

..#.#####..
###..#.#.##
..##..##.#.
..##..####.
###..#.#.##
..#.#####..
....##.####
..##.#.....
..#.##.####
#####...#..
#####......
###.#.#.#..
..#...#####

.##.#..#.#..##...
..#..##.......#..
###..###.#..##.##
###.#.#####....##
....#.###.###.###
##.#.#...##.##...
###.#.####.#.#...
..#.#.###.##..###
##.#.#.....#.....
.....##.##..#.###
..#.#..######.###
..#..##.#####.###
##..##.##..###.##

...#...##
.#....###
..#.#.#..
.#.###.##
.##......
#..#..#..
#...#####
#.#.###..
#.#.#.#..
.##...###
.##...###
..#.#.#..
#.#.###..

....####.##..##
#..###.#.#...##
#..###.#.#...##
....####.##..##
...##..##.#..#.
##.##.##....##.
#.#...##...#.##
..###.....#.#..
#.##.#..###.#..
...##.#....#..#
#...##.######..
##.###...#....#
##.#.##...##..#
####........###
####........###
##.#.##...##..#
#..###...#....#

..#......#..#..
..#......#..#..
##..####..##.##
.##########.#..
.#.#....#.#.###
##.######.###..
##.######.##...
..########.#.##
.#........#...#
....####......#
############...
####.##.####.##
.#.#....#.#.#..

##..###.#..##
#.##.#.###.#.
#.##.#.###.#.
##..###.#..##
.....#.#.##..
........#....
..##.....#..#
#.##.#.#..#..
.####..#.###.
.####..#.#.##
.####.#....#.

#..#..#.#.###
#...#.##.##.#
..##....#....
####..###...#
####..###...#
..###...#....
#...#.##.##.#
#..#..#.#.###
###.##...#...
.##..#.###.##
..##...##..##
..#.#..##...#
..#.#..##...#
..##...##..##
.##..#.###.##

##.##..
...#..#
...#..#
##.##..
#.#####
##.#...
##.#.##
..#..##
####.##

..#......#.#...
.##......##...#
##..####..####.
.....##.....###
##..#..#..##.#.
.#.##..##.#...#
#...#..#...#..#
#...#..#...#..#
.#.##..##.#...#
##..#..#..##.#.
.....##.....###
##..####..####.
.##......##...#

#.#..#...
#.#..#...
...####.#
.##....##
###....##
...####.#
#.#..#...

...#.#.##.#.#..
.#..#......#..#
#.##.#.##.#.##.
#.##.#.##.#.##.
.#..#......#..#
...#.#.##.#.#..
..#.#.#..#.#.#.
.#.#...##...#.#
.###.######.###
####.#....#.###
...#..####..#..
..#...#..#...#.
#...#.####.#...
#..##########..
#...##.##.##..#
#...#.#..#.#...
##.#.######.#.#

####....###
###.####.##
....#..#...
....####...
..#......#.
##...##...#
..########.
..###..###.
..##.##.##.
####.##.###
##..####..#
###..##..##
..##....##.
####.##..##
##...##...#
####....###
##..#..#..#

.##.###.###
.##.##..###
.##.##..###
.##.###.###
...#.#..#.#
..##...#...
##.#.#..#.#
#.##..#..#.
...###...#.
..#..##....
..#.##.####
......##...
##.#...#..#

......#..#...
...#.###.#...
##.#...###.##
##.#...###.##
...#.###.#...
...#..#..#...
###.####.#..#
###.#.#..##..
#######.#.###
##.##..#.###.
....##.#.##.#
###.###.#..#.
...#####...##

#.##...#.#..###
##.#..#.#....#.
#..#..#.#....#.
#.##...#.#..###
##.###.##..#...
...#......#...#
.#.....#..#.##.
.###..#...#.###
.#...#####..##.
.#...#####..##.
.###..#...#.###
.#.....#..#.##.
...#......#...#

...###..##..#
..###..###..#
..####.###..#
...###..##..#
..#...#.###..
..#...###.#..
..#..#.#.....
##..###.###.#
...##..#..#.#
...#..#..##..
###.##...#.##
..##.#.#..#..
..##.####.###

##.##.##...##..
#.#.#..###.##.#
#.#.#..###.##.#
##.##.##...##..
#..###..#..##..
##..##.###.##.#
.#..###...####.
.#.#####.#..#.#
#..#...##.#..#.

######.
..#....
##..#.#
.###.#.
#.#####
....#.#
....#.#
#.#####
.#.#.#.
##..#.#
..#....
######.
######.

##..#.#....
##..#.#....
..#.#.#....
#######.##.
#.###...##.
###.##..##.
..#........
.####.#....
#.##...##.#
####...####
..##.#..##.
..#.#......
..##.#.....

.##.##...
#...#.#..
.##....#.
........#
#..##..#.
.##.#.#.#
....#..#.
####..##.
####..#.#
####..#.#
####..##.

##..##.#..#.##.
####..#.##.#..#
..#.#...##...#.
.#..##.####.##.
#.##..##..##..#
.##.##.#..#.##.
.##....#..#....
#..#####..#####
#.#############
.#..##.####.##.
.#..##.#..#.##.
#..#..#.##.#..#
.######.##.####

.#..#...#####....
#.#.#.#.###...###
.#..##..#.#.#.#.#
.#######..#.#.###
...#.......######
.##...##.#.##..##
.#.##...###.#.###
.#.##...###.#.###
.##...##.#.##..##

###..####.#
###..####..
#....##.#..
#.....#.###
.#.##..###.
.#.##....#.
.##.##..#.#
.#..##.#...
...#.##.##.
...#.##.##.
.#..##.#...
.##.##..#.#
.#.##....#.
.#.##..###.
#.....#.###

.#.##.#
#......
.##..##
...##..
...##..
.##..##
#......
.######
.#....#
#.#..#.
###..##
..#..#.
#......
##....#
.######
##....#
.#....#

.#..#.#.##....#
.....#.##...#.#
.....#.##...#.#
.#..#.#.##....#
.####..#..##..#
...###...##.##.
..##.#..##..#..
##..#.#####...#
#.###.#.....#.#
#.#.##.##..##.#
#.#.##.##..##.#
#.###.#.....#.#
##..#.#####...#
..##.#..##..#..
...###...##..#.

..#.##.###.#.
#..##...#.#..
#.##...#..##.
#.###.##.#...
.#.##....#...
#.##.###..#..
......#.#.#.#
......#.#.#.#
#.##.###..#..
.#.##....#...
#.###.##.#...
#.##...#..##.
#..##...#.#.#
..#.##.###.#.
..#.##.###.#.

.##.#.#.##.
.##.##....#
.##.##....#
.##.#.#.##.
.##.##.#.##
#..#..#.#..
.....##.##.
.##.##.....
....###...#
.#####....#
#####.#...#
#####...#..
#..#.#.####
.##.#####.#
.##..##..##

...##.#..#.
.#.##.####.
.#...#.##.#
#.#########
..#########
##...#....#
##...#.##.#
..#########
#.#########

###..##..########
....#..#.#..####.
#.#..##..#.#....#
..#..##..#..#..#.
##.#....#.#######
###......###....#
.#.##..##.#.####.
#...####...######
.#.#.##.#.#......
###.####.###....#
#..........#....#
..#.####.#..#..#.
...##..##....##..
.#.##..##.#..##..
...##..##........
.#.#....#.#......
..##.##.##...##..

..#.#....##
......#....
...#...#.#.
.###..#.#..
.#.#.##..##
#..####..##
#..####..##

....#...#
###.#...#
#####..##
#######..
..#.##.#.
##..#....
###..##.#
###..##.#
##.##....

..##.#...#..#
..#..###..###
###.....#.#..
..##..#...#.#
##....#..##..
##....#..##..
..##..#...#.#
###.....###..
..#..###..###
..##.#...#..#
####...#..###
..#.##..#..##
..#...##.#...

..#..##.##..#.#
#####....#.##..
.#..##..######.
#####...##.####
..##.#.##....##
...#####.#.####
..##..#...#.###
.###..#...#.###
...#####.#.####
..##.#.##....##
#####...##.####
.#..##..######.
#####....#.##..
..#..##.##..#.#
.###..###.#.#.#
.###..###.#.#.#
..#..##.##..#.#

#...#.#..
#...#.#..
..##.#...
##..##...
.#...##..
#..###.##
#.#####..
.#....##.
.#..###..

#..##..#.#...##.#
......#....####.#
.##.####.######.#
........####.#..#
#####.#..##.#....
#..##..#.###..#.#
#..####.########.
#..####..#######.
#..##..#.###..#.#
#####.#..##.#....
........####.#..#

#...##.##.#..
##.##..###.##
#.######...##
##.#.########
.#....#......
#.#..##.##...
.##.#.##...##
##..###.#....
..####...#.##
.##.####..###
#...##.#.##..
#...##.#.##..
..#.####..###

#....#.
#.###..
#.###..
#....#.
..###..
.####..
.....#.
...#.#.
####..#
..###..
#...#..
......#
##...#.
##...#.
......#
#...#..
...##..

#..#..#.####.#.
..#.###.#####..
.....#.###...#.
..#....#.#.##.#
..##..##.#.####
..#####.....#..
..#####.....#..
.###..##.#.####
..#....#.#.##.#
.....#.###...#.
..#.###.#####..
#..#..#.####.#.
.#####.##.#..##
.#####.##.#..##
#..#..#.####.#.

......#
..##...
......#
.#..#.#
##..###
#....##
##..##.
##..###
##..###
##..##.
#....##
##..##.
.#..#.#
......#
..##...

#....##.#
.######.#
#.#..##.#
.#.###.##
.#.###.##
#.#..##.#
.######.#
#....##.#
#..###...
..#.#..#.
#.###.##.
###.#####
.###..##.
#.###.##.
#.###.##.
.####.##.
###.#####

.#.##.#.#..#.
.#.##.#.#....
##.##.##....#
..###...##..#
...##....#.##
.....##.##.##
###.....#.###
.##.###.#..#.
.##.###.#..#.
###.....#.###
.....##.##.##

######.######
.##....#...##
#####.#.##...
.##.#.###..##
.....#...#...
#..#####.#.##
#######.#....
.##...#..#.##
....##..###..
##.###...#...
.##.##.......
.....#.###...
#####.##...##
.##.......###
.##..##..##..

#......#..#....##
#..##..##....####
#.####.##..#.##.#
..#..#..#..#..#.#
.#....#..#.##..#.
##.##.###.##.####
........#.#...#..
.#....#.##.....#.
...........##..##
##.##.#####......
##..#.##.#..#.##.
#..##..#.#.####.#
#..##..#.#.####.#

.#..#..#..#
.###....###
#..#.##.#..
####....###
####....###
#..#.##.#..
.###.##.###

....#..##..#.....
.##.#......#.##..
.######..###.##..
.......##........
##.#........#.###
#..#..####..#..##
.##...####...##..
####........#####
..###.#..#.###...
.####.####.####..
.#..###..###..#..
.###..####..###..
..#.#.####.#.#...
..#.##.##.##.#...
##....####....###
#.##..####..##.##
###..#.##.#..####

.##.##.....##
#.#..#...#.#.
..##...##.###
..##...##.###
#.#..#...#.#.
.##.##....###
##..#.....#.#
.#..#..#.####
....#####.##.
....#####.##.
.#..#..#.####

#..#..######..#..
.##.#.#....#.#.#.
#.#.#...##...#.#.
.....##....##....
.#.#..#....#..#.#
#.....##..##.....
#.....##..##.....

.####.##.##.##.
..##...#....#..
.####.#.####.#.
.......######..
..##...........
#....#...##...#
.####...####...
.......#....#..
......#.####.#.
##..###########
######.##..##.#
.####.#.#..#.#.
......##....##.
#.##.##########
.......#.####..

#.#....#.#..#
.###..###.#..
.##....##...#
...#..#....##
#........#.#.
####..####...
....##....##.
....##....##.
####..####.#.

.###.#.###..#
.....#####.##
.#.##.##..##.
...##..#.##..
######...#...
######...#...
...##..#.##..
.#.##.##..##.
.....#####.##
.###.#.###..#
###...##.#.#.
..#..##.#.#.#
###.#..#...#.
#.##.##.#..##
#.##.##.#..##
###.#..#...#.
.....##.#.#.#

...#..#.#.#
#...#.#..##
...#.#.#.#.
#.###...#..
....#...##.
....#...##.
#.###...#..
...###.#.#.
#...#.#..##
...#..#.#.#
.#...###...
####....#..
####....#..
.#...###...
...#..#.#.#
#...#.#..##
...###.#.#.

.#...#.
.#...#.
#...#..
##.#..#
#####.#
..#....
##...##
##...##
#.#....
#####.#
##.#..#
#...#..
.#...#.

.....###......#
.##...#...#....
#..##..##.###..
....##.#....#.#
#####...###....
.##..##....#.#.
#..#..#..#...##
####.#.#####.#.
.##...##....#..
....#.##.#####.
....#.##.#####.
.##...##...##..
####.#.#####.#.
#..#..#..#...##
.##..##....#.#.
#####...###....
....##.#....#.#

.##..##..#.
.######..#.
#.####.##..
#.#....#.#.
.######.##.
#..##..#..#
###..###.##
#..##..#...
.#.##.#..#.
#.####.#...
.######..#.
#########.#
#.####.#...
.#.##.#..##
.######.##.
.######.##.
.#.##.#..##

#.#....###....#
#.#.####.######
.####.#...#..#.
#....#..#######
##.#.#....####.
#####..#.######
#####..#.######
##.#.#....####.
#.......#######

.#..##.##
#.....###
.##.#.###
#..#.#...
#..##..##
...##....
#...#..##
.####.#..
##..#####
.#....#..
.#..#....
......#..
......#..
.#..#....
.#...##..
##..#####
.####.#..

...##############
..##.....##......
#.....###.##.##.#
#.#.##.#####....#
##.#....#.....#..
#...#..##.#.####.
.##.#..#.##.#..#.
#...##..#..#....#
#...##..#..#....#

.##.#####
#...#..#.
#.#..##.#
##....#..
.#..##.#.
.#..##.#.
##....#..
#.#..##.#
#...#..#.
..#.#####
.##.#.##.
..#..#.##
#####..#.
#####..#.
..#..#.##

.#.#......#.#..
#..########..##
.####....####..
#..###..###..##
#.##..##..##.##
..#........#...
.############..
#..#.#..#.#..##
##.########.###
.##.###.##.##..
.#....##....#..
###...##...####
##..##..##..###

.##.#..#..#..
.......#..#..
.###.#.####.#
..####.#..#.#
......######.
.#####.#..#.#
.##..########
..##.#.#..#.#
....###....#.
#...#..#..#..
#...#..#..#..

##..#..#.
##..#..#.
#.###.##.
#..#...##
.#.#...##
.##....##
....##..#
....##..#
.##....##
.#.#...##
#..#...#.

##.##.#..
..#....#.
######.##
..####.#.
....#.##.
###.###..
..###.#.#
##...#.##
..##.#.##
##..#..#.
..#.###.#
....#..##
..#...##.
..###.##.
..#.##...
###.#.###
###.#####

##..##..#
.##.#.#.#
...#.##..
#..#.##..
.#####...
..##.####
..#..####
..#..####
..##.####

...####....
##......###
#.#....#.##
#.######.##
#..#..#..##
#.##..##.##
##..##..#..

.....##.###..###.
#....##.###..###.
.##....##.####.##
.#.##.#####..####
#.....#.###..###.
##..#.#..#.##.#..
##.#.....#....#..
#.#.#.##..####..#
####..###.#..#.##

.#..##.#.#####.
.#..##.#.#####.
#..#.#.###.#...
.#.#.#.##..#...
..#...#.#...##.
......#.####.##
###...##.#..###
##....##.#..###
......#.####.##

#.###.#
####...
.#....#
.#....#
####...
#.###.#
#.###..
###.###
.....##
.##..##
###...#
##....#
.##..##
.....##
###.###

#.##.##.##.#..#
..##....##..###
.####..####...#
.####..####..##
#.##.##.##.#..#
############.#.
############...
#.##.##.##.#...
############...
#.##.##.##.#.##
.####..####.##.
##..####..##...
#.##.##.##.####
#....##....###.
############.#.
............###
..###..###..##.

.#..#.#.#.#.#....
#########.##.####
#########.##.####
.#..#.#.#.#.##...
#.##.#.#..#.#....
..#####.#.#..#...
.##.#.#...##.#...
...###.#.##..#...
#.....###....#.#.
..#..####.##..##.
#.#..#...####....
#.#..#...####....
..#..####.##..##.
#.....###....#.#.
...###.#.##..#...
.##.#.#...##.#...
..#####.#.#..#...

.##.##.##..##
...####..##..
#..#.....##..
.##.##.#.##.#
####.#...##..
#..#####.##.#
.##.#.#.#..#.
######.######
....#.##.##.#

.#######..#..
...#.#.#...##
...#.#.#....#
.#######..#..
.#######..#..
...#.#.#....#
...#.#.#...##
.#######..#..
.#..#.#.##.#.
....####.....
#..##.#.#####
##...########
.##.#...#..#.

..#..##..##
..#..##..##
##...#.#.#.
#.#.#.#....
.###..####.
##.#.....##
..#.#.##..#
...#...##..
#########.#
#####.###.#
...#...##..
..#.#.##..#
##.#.....##
.###..####.
#.#.#.#....
""")
