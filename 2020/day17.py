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

	mx = 15
	def f(a):
		b = defaultdict(default)
		for i in range(-mx, mx):
			for j in range(-mx, mx):
				print(i, j)
				sys.stdout.flush()
				for k in range(-mx, mx):
					for l in range(-mx, mx):
						cnt = 0
						for ii in range(-1, 2):
							for jj in range(-1, 2):
								for kk in range(-1, 2):
									for ll in range(-1, 2):
										if ii == 0 and jj == 0 and kk == 0 and ll == 0: continue
										cnt += a[(i + ii, j + jj, k + kk, l + ll)]

						on = a[(i, j, k, l)] == 1
						if on:
							b[(i, j, k, l)] = 1 if 2 <= cnt <= 3 else 0
						else:
							b[(i, j, k, l)] = 1 if cnt == 3 else 0
		return b

	a = defaultdict(default)
	n = len(lines)
	for i in range(n):
		for j in range(n):
			if lines[i][j] == '#':
				a[(i, j, 0, 0)] = 1
	
	print(a)
	for i in range(6):
		a = f(a)			

	print(sum(a.values()))


if __name__ == "__main__":
	main()