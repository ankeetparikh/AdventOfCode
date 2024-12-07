from collections import deque
def solve(m, n, R):
	def isOpen(i, j):
		x, y = j, i
		t = x*x + 3*x + 2*x*y + y + y*y + R
		return bin(t).count('1') % 2 == 0
	
	src = (1, 1)
	d = {src:0}
	q = deque([src])
	snk = (n, m)
	
	while snk not in d and len(q):
		i, j = q.popleft()
		for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			ni, nj = i + di, j + dj
			if 0 <= ni and 0 <= nj and isOpen(ni, nj) and (ni, nj) not in d:
				d[(ni, nj)] = d[(i, j)] + 1
				q.append((ni, nj))
	print("Part 1:", d[snk])

	while len(q):
		i, j = q.popleft()
		for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			ni, nj = i + di, j + dj
			if 0 <= ni and 0 <= nj and isOpen(ni, nj) and (ni, nj) not in d:
				d[(ni, nj)] = d[(i, j)] + 1
				if d[(ni, nj)] < 50: 
					q.append((ni, nj))
	print("Part 2:", len(d))

# solve(7, 4, 10)

with open('../inputs/day13input.txt') as f:
  s = f.read()
solve(31, 39, int(s))