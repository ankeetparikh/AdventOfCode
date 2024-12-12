def solve(s):
  s = s.strip().split("\n")
  n, m = len(s), len(s[0])

  g = [(i, j) for i in range(n) for j in range(m) if s[i][j] == '#']
  r = [i for i in range(n) if '#' not in s[i]]
  c = [j for j in range(m) if '#' not in [s[i][j] for i in range(n)]]

  p1, p2 = 0, 0
  G = len(g)
  for i in range(G):
    for j in range(i + 1, G):
      x, y = g[i]
      a, b = g[j]
      p1 += abs(a - x) + abs(b - y)
      p2 += abs(a - x) + abs(b - y)
      for k in r:
        if min(a, x) < k < max(a, x):
          p1 += 1
          p2 += 1000000 - 1
      for k in c:
        if min(b, y) < k < max(b, y):
          p1 += 1
          p2 += 1000000 - 1
  print("Part 1:", p1)
  print("Part 2:", p2)

solve("""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""")

solve("""
.......#...........................................................................#........................................................
.............#...........#..................#.............................................................#..............#.......#..........
..................................................................#.........#......................................#........................
.................#...........................................................................................................#..............
.............................................................#..............................................................................
......................#.....................................................................#............................................#..
.....#...........................................#..........................................................................................
............................#..........................................#...............................#....................................
...........#......................................................................................#......................#..................
....................................................#.....#................................................#......................#.........
#..................................................................#.............#...........................................#..............
......................................#..................................................#...............................................#..
.................................#..........................................................................................................
...............#........#..............................................#...............................................#....................
.......#....................................................................................................................................
............................................................................#...................#..................#.......#.........#......
...................#......................#......#.......#.......#..........................................................................
............#...........................................................................#................#..................................
.....................................................#..................#................................................................#..
.............................#.....#..........................................................................#...................#.........
...#.......................................................#...............................#................................................
............................................#........................................................#......................................
...................................................................#..................................................................#.....
..........................................................................................................................#.................
#.......................#............................#.......................................#..............................................
..........................................#.................#.....................................#................................#........
..................#............................................................#........................#..............#....................
............................................................................................................................................
......#........................................................................................#.............................#..............
...............#........................#.........#.....#......#...................#..............................#.........................
.........................#.....#..........................................#.................................................................
.................................................................................................................................#..........
...........................................................#..................................................#..........#............#.....
.............#.................................................................#............................................................
.....................#............#..............#.......................................#..................................................
#..........................#...........................#..................................................#.................................
.............................................................#....................................................................#.......#.
......................................................................................................................#.....................
............#..................#...........#........#...............................#..............#...........#............................
.......#..............................#.....................................................................................................
........................#...............................................................#..............#.................#.............#....
.#..........................................................................................................#...............................
.........................................................#.....................#.................................................#..........
..........................................#..........................................#...........................#.........................#
.....#..........................#.................#..........#........#.....................................................................
..........#...........#.................................................................................#...................................
.............................................................................................................................#.......#......
..........................................................#.................#............#..................................................
.....................................................#..........................................#...........#...............................
.......................................#...............................#.............................#......................................
..................................#...............................................#........................................#.............#..
.......#.......#.......#..........................................#.........................................................................
.............................................#...............#..............................................................................
............................#................................................................#..............................................
........................................................#..................#.............................#........................#.........
...................................................................................................#..........#.............................
......#............................................................................#....................................#..................#
..................#.....#...............#.....#......#...................................#.....................................#............
..................................................................#...........#.............................................................
#.............#..........................................#...............#...................#.........#....................................
........#.............................................................................................................#.............#.......
......................#......................................#............................................................................#.
..............................#....................................................#........................................................
............................................................................................................................................
...............#.............................................................................................#..............................
........................#............#............................#................................................................#........
...#.....................................................#................#..............#...................................#..............
.............................................#..............................................................................................
...........................#................................................................................................................
.....................................................#......#....................................................#.....#....................
.....#....................................#.....#...........................#...................#...........................................
..............#.....................#...................................................................#...................................
#........................................................................................#..................................................
.....................#........................................................................................#.............................
..........................#.......................#..................................................................................#......
.........#................................................#.........#.......................................................#...............
...............................#................................................................#.....#.....................................
...................#..........................#.................#..................#..............................................#.........
......#......#..............................................................................................................................
............................#......................................................................#........#...............................
....................................................................................................................#.......................
................................................#...........#.................#........................#....................................
.................#..........................................................................................................................
..........................#......................................................................................#..........#..........#....
#...............................................................................................#.....................#.....................
............#......................#...................#.................................#.........................................#........
............................................................................................................................................
....................................................................#.......................................................................
.....#........................................#...........................................................#...................#.............
..........................................................#..................................#..............................................
.............................#............................................#.................................................................
......................#............................................................................................................#........
..#.....................................................................................................................................#...
...........#..........................#............................................................................#........................
..............................................#.................#....................#...............#........#.............................
...........................#...........................#......................................#...........................#.....#...........
.........................................................................................................#..................................
.........#......#................................................................................................#........................#.
...#.....................................................................#..............#...................................................
.............................#......#...............................#................................................#......................
.........................................#............................................................................................#.....
.....................#............................#............#.................#...........................#...............#..............
.............#..........................................#...................................#...............................................
..#.............................#...........................................#.....................#................#........................
...........................................#...........................#.................................................#..............#...
........#...........................#.......................#.......................#.......................................................
...........................#.............................................................................#.......................#..........
............................................................................................................................................
...............#...............................................................................#..........................................#.
............................................................................................................................................
#...............................................#......#.......#...............#............................................................
.........#.................................#...........................................................#....................................
......................................#............................#...............................................#........................
......................#.........#.............................................................................#.............................
....................................................................................#............#..........................................
..........................................................................#...............#.................................................
...........#.....#................................#.........................................................................#...............
..................................................................#.......................................#.........................#.......
.........................#................................#........................................................#........................
........#...................................................................................#......#....................................#...
...............................................................#...............#............................................................
.............................................#.........................#.....................................#..............................
...................#...............#........................................................................................................
..........................#..............................#....................................#..................................#..........
...........#.....................................................................#.....#....................................................
...#.................................................#...............................................#...........#...........#..............
...............#........................#................................................................................................#..
....................#..............................................#.....................................#..................................
..................................#.....................#................................#..................................................
............................................#...................................................#.............#.............................
........................................................................................................................#.....#......#.....#
...........................................................#..................#......................#......................................
...................#.........#....................................#.........................#...............................................
....................................................#...............................................................#.......................
.............#........................#....................................................................................#................
....................................................................................#...................................................#...
.......#................................................#................#..................................................................
.#.................................................................#..............................................................#.........
...................#.....#...................................................................#.........#.........#..........................
............................................#.....#............#..................................#.........#................#..............
""")