import itertools

def gen():
  yield 0, 0
  k = 1
  while True:
    x, y = k, -k + 1
    dx, dy = 0, 1
    s = 2 * k
    for i in range(4):
      for j in range(s):
        yield x, y
        x, y = x + dx, y + dy
      dx, dy = -dy, dx
    k += 1

def solve1(n):
    a = list(itertools.islice(gen(), 12))
    print(a)
    x, y = a[-1]
    print(abs(x) + abs(y))

def solve2(s):
  pass

def solve(s):
  solve1(s)
  solve2(s)

solve1(5)