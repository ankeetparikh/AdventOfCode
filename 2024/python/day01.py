with open('../inputs/day01input.txt') as f:
  contents = f.read()

a = [list(map(int, line.split())) for line in contents.split("\n")]
l1 = [x for x, y in a]
l2 = [y for x, y in a]

l1.sort()
l2.sort()

p1 = sum(abs(x - y) for x, y in zip(l1, l2))
print("Part 1:", p1)

p2 = sum(x * l2.count(x) for x in l1)
print("Part 2:", p2)