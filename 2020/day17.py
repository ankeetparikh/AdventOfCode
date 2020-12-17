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
	lines = [line.strip() for line in file.readlines()]

	def f(a):
		nei = defaultdict(default)
		for i, j, k, l, in a:
			for ii, jj, kk, ll in itertools.product([-1, 0, 1], repeat = 4):
				if (ii, jj, kk, ll) == (0, 0, 0, 0): continue
				nei[(i + ii, j + jj, k + kk, l + ll)] += 1
		b = set()
		for (i, j, k, l), cnt in nei.items():
			if (i, j, k, l) in a:
				if 2 <= cnt <= 3:
					b.add((i, j, k, l))
			else:
				if cnt == 3:
					b.add((i, j, k, l))
		return b

	a = set()
	n = len(lines)
	for i in range(n):
		for j in range(n):
			if lines[i][j] == '#':
				a.add((i, j, 0, 0))
	
	print(a)
	for i in range(6):
		a = f(a)			

	print(len(a))


if __name__ == "__main__":
	main()