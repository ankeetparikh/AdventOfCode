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

	[card, door] = [int(x) for x in file.read().split("\n")]

	mod = 20201227

	def dL(a, b):
		aa = 1
		i = 0
		while aa != b:
			aa = (aa * a) % mod
			i += 1
		return i

	cloop = dL(7, card)
	dloop = dL(7, door)

	print(pow(card, dloop, mod))

	
if __name__ == "__main__":
	main()