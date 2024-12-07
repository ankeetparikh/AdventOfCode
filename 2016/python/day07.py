import re

def solve1(s):
	s = s.strip().split("\n")
	def has(t):
		for i in range(len(t) - 3):
			if t[i] == t[i + 3] and t[i + 1] == t[i + 2] and t[i] != t[i + 1]:
				return True
		return False
	cnt = 0
	for x in s:
		x = x.replace("[", "*").replace("]", "*")
		y = x.split("*")
		u, v = 0, 0
		for i, z in enumerate(y):
			if has(z):
				if i % 2 == 0:
					u = 1
				else:
					v = 1
		cnt += 1 if u and not v else 0
	print("Part 1:", cnt)

def solve2(s):
	s = s.strip().split("\n")
	def has(t):
		for i in range(len(t) - 3):
			if t[i] == t[i + 3] and t[i + 1] == t[i + 2] and t[i] != t[i + 1]:
				return True
		return False
	cnt = 0
	for x in s:
		x = x.replace("[", "*").replace("]", "*")
		y = x.split("*")
		ALPHA = [chr(i) for i in range(ord('a'), ord('z') + 1)]
		sup = 0
		for a in ALPHA:
			for b in ALPHA:
				if a == b: continue
				A = f"{a}{b}{a}"
				B = f"{b}{a}{b}"
				if any(A in t for t in y[0::2]) and any(B in t for t in y[1::2]):
					sup = 1
		cnt += sup
	print("Part 2:", cnt)

def solve(s):
	solve1(s)
	solve2(s)

with open('../inputs/day07input.txt') as f:
  s = f.read()
solve(s)