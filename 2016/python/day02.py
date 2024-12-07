def solve1(s):
	s = s.strip().split("\n")
	z = {}
	for i in range(3): 
		for j in range(3): 
			z[(i, j)] = 3 * i + j + 1
	def get(x, y, nx, ny):
		if 0 <= nx and nx < 3 and 0 <= ny and ny < 3: return nx, ny
		return x, y
	x, y = 1, 1
	res = []
	for line in s:
		for op in line:
			if op == 'U': x, y = get(x, y, x - 1, y)
			if op == 'D': x, y = get(x, y, x + 1, y)
			if op == 'L': x, y = get(x, y, x, y - 1)
			if op == 'R': x, y = get(x, y, x, y + 1)
		res.append(str(z[(x, y)]))
	print("Part 1:", ''.join(res))

def solve2(s):
	s = s.strip().split("\n")
	z = {}
	
	z[0] = {2: 1}
	z[1] = {1: 2, 2: 3, 3: 4}
	z[2] = {0: 5, 1:6, 2:7, 3:8, 4:9}
	z[3] = {1:'A', 2:'B', 3:'C'}
	z[4] = {2:'D'}

	def get(x, y, nx, ny):
		if nx in z and ny in z[nx]: return nx, ny
		return x, y

	x, y = 2, 0
	res = []
	for line in s:
		for op in line:
			if op == 'U': x, y = get(x, y, x - 1, y)
			if op == 'D': x, y = get(x, y, x + 1, y)
			if op == 'L': x, y = get(x, y, x, y - 1)
			if op == 'R': x, y = get(x, y, x, y + 1)
		res.append(str(z[x][y]))
	print("Part 2:", ''.join(res))

def solve(s):
	solve1(s)
	solve2(s)

# solve(
# '''
# ULL
# RRDDD
# LURDL
# UUUUD
# '''
# )

with open('../inputs/day02input.txt') as f:
  s = f.read()
solve(s)