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
	[p1, p2] = file.read().split("\n\n")
	p1 = list(map(int, p1.split("\n")[1:]))
	p2 = list(map(int, p2.split("\n")[1:]))

	def rec(p1, p2):
		mem = set()
		winner = 0
		while len(p1) > 0 and len(p2) > 0:
			if (tuple(p1), tuple(p2)) in mem:
				winner = 1
				break
			mem.add((tuple(p1), tuple(p2)))
			a = p1[0]
			b = p2[0]
			p1 = p1[1:] if len(p1) > 0 else []
			p2 = p2[1:] if len(p2) > 0 else []

			if a <= len(p1) and b <= len(p2):
				[rwinner, _] = rec(p1[0:a], p2[0:b])
				if rwinner == 1:
					p1.extend([a, b])
				else:
					p2.extend([b, a])
			else:
				if a > b:
					p1.extend([a, b])
				else:
					p2.extend([b, a])
		
		if winner == 0:
			winner = 1 if len(p1) > 0 else 2
		p1.extend(p2)
		return (winner, p1)

	def calc(a):
		n = len(a)
		c = 0
		for i, x in enumerate(a):
			c += (n - i) * x
		return c

	# print("Part 1 =", calc(rec(p1, p2)))

	[winner, res] = rec(p1, p2)
	print(winner)
	print(res)
	print("Part 2 =", calc(rec(p1, p2)[1]))
	
if __name__ == "__main__":
	main()