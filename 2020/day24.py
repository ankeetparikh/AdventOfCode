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
	tiles = file.read().split("\n")
	
	dirs = ["e", "w", "se", "sw", "ne", "nw"]
	vecs = {
		"e": (1, 0),
		"w": (-1, 0),
		"se": (1, -1),
		"sw": (0, -1),
		"ne": (0, 1),
		"nw": (-1, 1)
	}

	color = defaultdict(int)
	
	def toggle(s):
		x,y = 0,0
		while len(s) > 0:
			for d in dirs:
				if s.startswith(d):
					x += vecs[d][0]
					y += vecs[d][1]
					s = s[len(d):]
					break
		color[(x, y)] ^= 1


	for s in tiles:
		toggle(s)

	print("Part 1 =", sum(color.values()))


	def neib(x, y):
		cnt = 0
		for (xx, yy) in vecs.values():
			cnt += color[(x + xx, y + yy)]
		return cnt
	def getN(x, y):
		cnt = neib(x, y)
		if color[(x, y)] == 1:
			return 1 if cnt == 1 or cnt == 2 else 0
		else:
			return 1 if cnt == 2 else 0

	for i in range(100):
		change = defaultdict(int)
		checks = [u for u in color.keys()]
		for (x, y) in checks:
			change[(x, y)] = getN(x, y)
			for (xx, yy) in vecs.values():
				change[(x + xx, y + yy)] = getN(x + xx, y + yy)
		tmp = defaultdict(int)
		for (x, y) in change:
			if change[(x, y)] == 1:
				tmp[(x, y)] = 1
		color = tmp

	# print(color)

	print("Part 2 =", sum(color.values()))

	
if __name__ == "__main__":
	main()