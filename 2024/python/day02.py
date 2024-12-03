with open('../inputs/day02input.txt') as f:
  contents = f.read()

a = [list(map(int, line.split())) for line in contents.split("\n")]

def safe(r):
  inc = all(x < y for x, y in zip(r, r[1:]))
  dec = all(x > y for x, y in zip(r, r[1:]))
  dif = all(1 <= abs(x - y) <= 3 for x, y in zip(r, r[1:]))
  return (inc or dec) and dif

p1 = sum(1 if safe(r) else 0 for r in a)

print("Part 1:", p1)

p2 = 0
for r in a:
  if any(safe(r[:i] + r[i + 1:]) for i in range(len(r) + 1)):
    p2 += 1
print("Part 2:", p2)