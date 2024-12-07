with open('../inputs/day01input.txt') as f:
  s = f.read()

s = s.replace(",", "").strip().split()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
x, y = 0, 0
found, fx, fy = 0, 0, 0
vis = set((0, 0))
for o in s:
	t = o[0]
	a = int(o[1:])

	if t == 'L':
		d = (d + 3) % 4
	else:
		d = (d + 1) % 4
	for i in range(a):
		x += dirs[d][0]
		y += dirs[d][1]
		if (x, y) in vis and not found:
			found = 1
			fx, fy = x, y
		vis.add((x, y))

print("Part 1:", abs(x) + abs(y))
print("Part 2:", abs(fx) + abs(fy))
