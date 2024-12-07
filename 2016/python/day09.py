import numpy as np

def solve1(s):
	s = s.strip().split("\n")
	a = s[0]
	n = len(a)
	i = 0
	tot = 0
	while i < n:
		if a[i] == '(':
			j = a.find(')', i + 1)
			L, R = list(map(int, a[i + 1 : j].split("x")))
			tot += L * R
			i = j + L + 1
		else:
			tot += 1
			i += 1
	print("Part 1:", tot)

def solve2(s):
	def get_len(a):
		n = len(a)
		i = 0
		tot = 0
		while i < n:
			if a[i] == '(':
				j = a.find(')', i + 1)
				L, R = list(map(int, a[i + 1 : j].split("x")))
				tot += get_len(a[j + 1: j + 1 + L]) * R
				i = j + L + 1
			else:
				tot += 1
				i += 1
		return tot
	s = s.strip().split("\n")
	a = s[0]

	print("Part 2:", get_len(a))

def solve(s):
	solve1(s)
	solve2(s);

# solve(
# '''
# A(2x2)BCD(2x2)EFG
# '''
# )

with open('../inputs/day09input.txt') as f:
  s = f.read()
solve(s)