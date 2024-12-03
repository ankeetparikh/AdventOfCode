def solve1(s):
  s = s.strip().split("\n")
  t = list(map(int, s[0].split(":")[1].split()))
  d = list(map(int, s[1].split(":")[1].split()))
  n = len(t)
  ans = 1
  for i in range(n):
    T = t[i]
    D = d[i]
    w = 0
    for i in range(1, T + 1):
      K = i * (T - i)
      if K > D: w += 1
    ans *= w
  print(ans)

def solve2(s):
  pass
def solve(s):
  solve1(s)
  solve2(s)

solve1("""Time:      7  15   30
Distance:  9  40  200
""")

solve1("""Time:      71530
Distance:  940200
""")

solve1("""Time:        48 87 69 81
Distance:   255 1288 1117 1623
""")

solve1("""Time:        48876981
Distance:   255128811171623
""")