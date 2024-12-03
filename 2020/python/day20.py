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
	tiles = file.read().split("\n\n")
	tmp = {}
	for tile in tiles:
		[idx, bd] = tile.split("\n", 1)
		idx = int(idx.split()[1][:-1])
		bd = bd.split("\n")
		tmp[idx] = bd

	tiles = tmp
	N = len(tiles)
	S = int(N**0.5)
	s = 10
	
	rot90 = {}
	def comp_rot(side):
		for i in range(side):
			for j in range(side):
				(ii, jj) = (i + 1, j + 1)
				(ii, jj) = (-jj, ii)
				ii += side
				jj -= 1
				rot90[(side, i, j)] = (ii, jj)

	def get_pos(i, j, r, side=s):
		if r < 4:
			for iter in range(r):
				(i, j) = rot90[(side, i, j)]
		elif r == 4:
			i = side - i - 1
		elif r == 5:
			j = side - j - 1
		elif r == 6:
			i, j = j, i
		elif r == 7:
			i, j = (side - j - 1, side - i - 1)
		return i, j

	def get(idx, i, j, r):
		i, j = get_pos(i, j, r)
		return tiles[idx][i][j]

	@functools.lru_cache(maxsize = 144 * 8 * 144 * 8)
	def above(a, u, b, v):
		for p in range(s):
			if get(a, s - 1, p, u) != get(b, 0, p, v):
				return False
		return True

	@functools.lru_cache(maxsize = 144 * 8 * 144 * 8)
	def left(a, u, b, v):
		for p in range(s):
			if get(a, p, s - 1, u) != get(b, p, 0, v):
				return False
		return True


	comp_rot(s)
	cnt = defaultdict(int)
	g = defaultdict(list)
	p = 1
	corner = 0
	for idx, bd in tiles.items():
		nei = set()
		for id2 in tiles.keys():
			if id2 == idx: continue
			for r in range(8):
				if above(idx, 0, id2, r) or above(id2, r, idx, 0) or left(idx, 0, id2, r) or left(id2, r, idx, 0):
					nei.add(id2) 
		cnt[len(nei)] += 1
		g[idx] = list(nei)
		if len(nei) == 2:
			print(idx)
			corner = idx
			p *= idx


	print("Part 1 =", p)
	

	# determine which tile goes where, and what their rotations are
	cur = [[0 for i in range(S)] for j in range(S)]
	rot = [[-1 for i in range(S)] for j in range(S)]

	
	cur[0][0] = corner
	cur[0][1] = g[corner][0]
	cur[1][0] = g[corner][1]

	used = set()
	used.add(cur[0][0])
	used.add(cur[0][1])
	used.add(cur[1][0])
	
	for idx in g[cur[0][1]]:
		if idx in g[cur[0][1]] and idx in g[cur[1][0]] and idx not in used:
			cur[1][1] = idx
			used.add(cur[1][1])
			break

	for j in range(2, S):
		for idx in g[cur[0][j - 1]]:
			if idx not in used:
				cur[0][j] = idx
				used.add(cur[0][j])
				for id2 in g[idx]:
					if id2 in g[cur[1][j - 1]] and id2 not in used:
						cur[1][j] = id2
						used.add(cur[1][j])
						break
				break
	for i in range(2, S):
		for j in range(S):
			for idx in g[cur[i - 1][j]]:
				if idx not in used:
					cur[i][j] = idx
					used.add(cur[i][j])
					break

	for i in range(8):
		for j in range(8):
			for k in range(8):
				if above(cur[0][0], i, cur[1][0], j) and left(cur[0][0], i, cur[0][1], k):
					rot[0][0] = i
					rot[1][0] = j
					rot[0][1] = k

	for j in range(2, S):
		for r in range(8):
			if left(cur[0][j - 1], rot[0][j - 1], cur[0][j], r):
				rot[0][j] = r
	for i in range(1, S):
		for j in range(S):
			for r in range(8):
				if above(cur[i - 1][j], rot[i - 1][j], cur[i][j], r):
					rot[i][j] = r
	
	print("Tile Indexes:")
	for vec in cur:
		print(vec)

	print("Tile Rotations:")
	for vec in rot:
		print(vec)

	rot_val = {}
	for i in range(S):
		for j in range(S):
			rot_val[cur[i][j]] = rot[i][j];
	# fill in the board
	tile_nob = {}
	for idx, tile in tiles.items():
		rotated = []
		for i in range(s):
			tilerow = ""
			for j in range(s):
				tilerow += get(idx, i, j, rot_val[idx])
			rotated.append(tilerow)
		tmp = []
		for i in range(1, s - 1):
			tmp.append(rotated[i][1:s-1])
		tile_nob[idx] = tmp
	
	board = ["" for i in range(S * (s - 2))]
	for i in range(S):
		for j in range(S):
			for k in range(s - 2):
				board[8 * i + k] += tile_nob[cur[i][j]][k]
	
	print("BOARD:")
	for row in board:
		print(row)

	monster = [
		"                  # ",
		"#    ##    ##    ###",
		" #  #  #  #  #  #   "
	]

	comp_rot(len(board))
	A = len(monster)
	B = len(monster[0])
	L = len(board)
	POUNDS = sum(1 if board[i][j] == '#' else 0 for i in range(L) for j in range(L))
	for r in range(8):
		rotated = []
		for i in range(L):
			rotated.append("")
			for j in range(L):
				u, v = get_pos(i, j, r, L)
				rotated[i] += board[u][v]
		copy = [[char for char in word] for word in rotated]
		num_monsters = 0
		for i in range(L - A + 1):
			for j in range(L - B + 1):
				good = True
				for a in range(A):
					for b in range(B):
						if monster[a][b] == '#' and rotated[i + a][j + b] != '#':
							good = False
				if good:
					num_monsters += 1
					for a in range(A):
						for b in range(B):
							if monster[a][b] == '#':
								copy[i + a][j + b] = '.'
		if num_monsters != 0:
			print("number of monsters =", num_monsters)
			print("pounds not part of monsters =", sum(1 if copy[i][j] == '#' else 0 for i in range(L) for j in range(L)))

if __name__ == "__main__":
	main()