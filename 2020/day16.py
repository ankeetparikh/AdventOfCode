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
	[rule, me, a] = file.read().split("\n\n")

	rule = rule.split("\n")
	for i in range(len(rule)):
		rule[i] = rule[i].split(":")[1]
		rule[i] = rule[i].split("or")
		rule[i] = [x.strip() for x in rule[i]]
		tmp = []
		for elem in rule[i]:
			v = []
			for x in elem.split("-"):
				v.append(int(x))
			tmp.append(v)
		rule[i] = tmp
		# print(rule[i])

	a = a.split("\n")[1:]
	for i in range(len(a)):
		a[i] = [int(x) for x in a[i].split(",")]

	g = []
	for arr in a:
		has_inv = False
		for x in arr:
			valid = 0
			for r in rule:
				for L, R in r:
					if L <= x <= R:
						valid = 1
			if valid == 0:
				has_inv = True
		if not has_inv:
			g.append(arr)

	n = len(g)
	cnt = defaultdict(default)
	for arr in g:
		for i, x  in enumerate(arr):
			for j, y in enumerate(rule):
				works = 0
				for L, R in y:
					if L <= x <= R:
						works = 1
				cnt[(i, j)] += works
	
	# print(g)
	P = len(rule)
	p = []

	def rec():
		if len(p) == P:
			return True

		for i in range(P):
			if cnt[(len(p), i)] == n and i not in p:
				p.append(i)
				if rec():
					return True
				else:
					p.pop()
		return False
	rec()

	print("p = ", p)

	me = me.split("\n")[1]
	me = [int(x) for x in me.split(",")]


	prod = 1
	for (a, b) in zip(p, me):
		if a < 6:
			prod *= b
	print(prod)

if __name__ == "__main__":
	main()
