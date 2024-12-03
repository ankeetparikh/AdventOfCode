s = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2"

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
