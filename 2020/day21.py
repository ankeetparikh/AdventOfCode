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
	file = open("in.txt")
	# file = open("sample.txt", "r")
	lines = file.read().split("\n")
	L = len(lines)
	for i in range(L):
		[a, b] = lines[i].split("(contains")
		b = b.replace(")", "")
		a = a.split()
		b = b.split(",")
		a = [x.strip() for x in a]
		b = [x.strip() for x in b]
		lines[i] = [a, b]
	
	alg = set()
	ing = set()
	for u, v in lines:
		for ingr in u:
			ing.add(ingr)
		for allergen in v:
			alg.add(allergen)

	g = defaultdict(list)
	for a in alg:
		for u, v in lines:
			if a not in v: continue
			g[a].append(u)

	can = set()
	h = {}
	for k, v in g.items():
		choices = list(functools.reduce(set.intersection, [set(item) for item in v]))
		for x in choices:
			can.add(x)
		h[k] = choices


	c = 0
	for u, v in lines:
		for ingr in u:
			if ingr not in can:
				c += 1
	print("Part 1 =", c)
	n = len(alg)
	ans = []
	while len(ans) < n:
		know = ""
		for a, ch in h.items():
			if len(ch) == 1:
				know = a
		al = h[know][0]
		ans.append((know, al))

		hh = h
		for a, ch in h.items():
			if al in ch:
				hh[a].remove(al)

		h = hh

	ans.sort()
	st = ""
	for u, v in ans:
		if len(st) > 0:
			st += ","
		st += v
	print("Part 2 =", st)

	
if __name__ == "__main__":
	main()