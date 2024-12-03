import numpy as np
def solve(g):
	L = 300
	z = np.zeros((L + 1, L + 1), dtype=int)
	for y in range(1, L + 1):
		for x in range(1, L + 1):
			z[y][x] = (((x + 10) * y + g) * (x + 10) // 100) % 10 - 5
	xx, yy, best = -1, -1, -10**50
	for y in range(1, L + 1 - 2):
		for x in range(1, L + 1 - 2):
			s = z[y:y+3, x:x+3].sum()
			if s > best: xx, yy, best = x, y, s
	print(f"Part 1: {xx},{yy}")
	
	d = np.zeros((L + 1, L + 1), dtype = int)
	for y in range(1, L + 1):
		for x in range(1, L + 1):
			d[y][x] = z[y][x] + d[y][x - 1] + d[y - 1][x] - d[y - 1][x - 1]
	xx, yy, best, k = -1, -1, -10**50, -1
	for kk in range(1, L + 1):
		for y in range(kk, L + 1):
			for x in range(kk, L + 1):
				s = d[y][x] - d[y][x - kk] - d[y - kk][x] + d[y - kk][x - kk]
				if s > best: xx, yy, best, k = x - kk + 1, y - kk + 1, s, kk
	print(f"Part 2: {xx},{yy},{k}")

# solve(18)
solve(3613)