def solve1(s):
	s = s.strip().split("\n")
	cnt = 0
	for line in s:
		x = sorted(list(map(int, line.split())))
		if x[0] + x[1] > x[2]: cnt += 1
	print("Part 1:", cnt)

def solve2(s):
	s = s.strip().split("\n")
	s = [list(map(int, x.split())) for x in s]
	cnt = 0
	for i in range(3):
		for j in range(len(s) // 3):
			x = sorted([s[3 * j][i], s[3 * j + 1][i], s[3 * j + 2][i]])
			if x[0] + x[1] > x[2]: cnt += 1
	print("Part 2:", cnt)

def solve(s):
	solve1(s)
	solve2(s)

with open('../inputs/day03input.txt') as f:
  s = f.read()
solve(s)