from collections import defaultdict
import itertools
import json
import sys
import re
def popcount(x):
	return x if x < 2 else (popcount(x // 2) + (x & 1));
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

file = open("in.txt", "r")
lines = [line.strip() for line in file.readlines()]

def apply(mask, v):
	x = [c for c in mask]
	for i in range(36):
		a = v >> (36 - i - 1) & 1
		if x[i] == '0':
			x[i] = '1' if a == 1 else '0'
	return "".join(x)


mem = {}
mask = ['X' for i in range(36)]

def rec(cur, mask, i, v):
	if i == 36:
		mem[cur] = v
		return
	if mask[i] == 'X':
		rec(cur, mask, i + 1, v)
		rec(cur | (1 << (36 - i - 1)), mask, i + 1, v)
	elif mask[i] == '0':
		rec(cur, mask, i + 1, v)
	elif mask[i] == '1':
		rec(cur | (1 << (36 - i - 1)), mask, i + 1, v)

for line in lines:
	if "mask" in line:
		[_, _, mask] = line.split()
	else:
		[u, _, v] = line.split()
		i = int(u[4:-1])
		v = int(v)
		rec(0, apply(mask, i), 0, v)

s = 0
for k in mem:
	s += mem[k]

print(s)