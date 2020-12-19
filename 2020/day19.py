from collections import defaultdict
import itertools
import functools
import operator
import json
import sys
import re
import math
import random

def popcount(x):
	return x if x < 2 else (popcount(x // 2) + (x & 1))
def prod(x):
	return functools.reduce(operator.mul, x, 1)
def default():
	return 0
def defaultList():
	return []
def neighbors(x, y, diag = False):
	vectors = [
		[(1, 0), (-1, 0), (0, 1), (0, -1)],
		[(1, 1), (1, 0), (1, -1), (0, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
	][diag]
	print(vectors)
	return [(x + vectors[i][0], y + vectors[i][1]) for i in range(len(vectors))]

# solution begins here 

def main():
	file = open("in.txt", "r")
	[rules, messages] = file.read().split("\n\n")
	# lines = [line.strip() for line in file.readlines()]
	rules = rules.split("\n")
	messages = messages.split("\n")
	g = {}
	for rule in rules:
		[i, st] = rule.split(":")
		if "\"" in st:
			g[int(i)] = st.strip().replace("\"", "")
		else:
			st = st.strip().split("|")
			h = []
			for s in st:
				u = []
				for x in s.strip().split():
					u.append(int(x))
				h.append(u)
			g[int(i)] = h

	done = {}

	def solve_rep(x):
		x.sort(key=lambda x: x[0])
		d = defaultdict(list)
	
		for u, v in x:
			if u - 1 in d:
				for b, num in d[u - 1]:
					d[v].append((b, num + 1))
			d[v].append((u, 1))
		res = {}
		for v, vec in d.items():
			for u, num in vec:
				res[(u, v)] = num
		return res

	def solve11(x, y):
		res = set()
		for (u, v), num in x.items():
			for (uu, vv), nnum in y.items():
				if num == nnum and v + 1 == uu:
					res.add((u, vv))
		return list(res)

	def find(i, s):
		if i in done:
			return done[i]
		if i == 8:
			res = solve_rep(find(42, s))
			done[i] = res.keys()
			return done[i]
		if i == 11:
			done[i] = solve11(solve_rep(find(42, s)), solve_rep(find(31, s)))
			return done[i]
		if g[i] == "a" or g[i] == "b":	
			res = []
			for j in range(len(s)):
				if s[j] == g[i]:
					res.append((j, j))
			done[i] = res
			return res
		else:
			res = []
			for a in g[i]:
				if len(a) == 1:
					res.extend(find(a[0], s))
				else:
					h = [find(j, s) for j in a]
					if any(len(j) == 0 for j in h):
						continue
					for t in itertools.product(*h):
						bad = False
						for j in range(1, len(t)):
							if t[j - 1][1] + 1 != t[j][0]:
								bad = True
								break
						if not bad:
							res.append((t[0][0], t[len(t)-1][1]))
			res = list(set(res))
			done[i] = res
			return res

	def matches(s):
		done.clear()
		result = find(0, s)
		# print(result)
		# print("done[8] = ", done[8])
		# print("done[42] = ", done[42])
		# print("g[8] = ", g[8])
		# print("g[42] = ", g[42])
		return (0, len(s) - 1) in result

	print(sum(1 if matches(line) else 0 for line in messages[0:]))

if __name__ == "__main__":
	main()