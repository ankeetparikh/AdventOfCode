import numpy as np

def solve(s):
	s = s.strip().split("\n")
	N, M = 6, 50
	a = np.zeros((N, M))

	for line in s:
		if "rect" in line:
			m, n = list(map(int, line.split()[1].split('x')))
			for i in range(n):
				for j in range(m):
					a[i][j] = 1
		else:
			y = line.split()
			idx = int(y[2][y[2].find("=") + 1:])
			amt = int(y[4])
			
			if y[1] == 'row':
				a[idx] = np.roll(a[idx], amt)
			else:
				a[:, idx] = np.roll(a[:, idx], amt)
			pass
	cnt = 0
	for i in range(N):
		for j in range(M):
			cnt += a[i][j] == 1

	print("Part 1:", cnt)
	print("Part 2:")
	for i in range(N):
		for j in range(M):
			if a[i][j]: 
				print("X", end='')
			else:
				print(" ", end='') 
		print("")

with open('../inputs/day08input.txt') as f:
  s = f.read()
solve(s)