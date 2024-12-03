import fluentpy as _
import re
from collections import *
from itertools import *
from math import *
from functools import *
import string
import numpy as np
import heapq

def solve1(s):
	A = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	inf = 10**20
	N, M = len(A), len(A[0])
	sx, sy, ex, ey = 0, 0, 0, 0
	best = np.zeros((N, M), dtype=np.int64)
	for i in range(N):
		for j in range(M):
			best[i][j] = 10**9
			if A[i][j] == 'S':
				sx, sy = i, j
			if A[i][j] == 'E':
				ex, ey = i, j

	vis = set()
	best[sx][sy] = 0
	q = []
	heapq.heappush(q, (0, sx, sy))
	while len(q):
		d, x, y = heapq.heappop(q)
		vis.add((x, y))
		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nx, ny = x + dx, y + dy
			if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in vis:
				originheight = ord('a') if A[x][y] == 'S' else ord(A[x][y])
				destheight = ord('z') if A[nx][ny] == 'E' else ord(A[nx][ny])
				# print("got here", x, y, nx, ny)
				if originheight + 1 >= destheight and d + 1 < best[nx][ny]:
					best[nx][ny] = d + 1
					heapq.heappush(q, (d + 1, nx, ny))
	# print(best)
	print(best[ex][ey])

def solve2(s):
	A = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	inf = 10**20
	N, M = len(A), len(A[0])
	sx, sy, ex, ey = 0, 0, 0, 0
	best = np.zeros((N, M), dtype=np.int64)
	for i in range(N):
		for j in range(M):
			best[i][j] = 10**9
			if A[i][j] == 'S':
				sx, sy = i, j
			if A[i][j] == 'E':
				ex, ey = i, j

	vis = set()
	q = []
	for i in range(N):
		for j in range(M):
			if A[i][j] == 'a' or A[i][j] == 'S':
				vis.add((i, j))
				best[i][j] = 0
				heapq.heappush(q, (0, i, j))
	while len(q):
		d, x, y = heapq.heappop(q)
		vis.add((x, y))
		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nx, ny = x + dx, y + dy
			if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in vis:
				originheight = ord('a') if A[x][y] == 'S' else ord(A[x][y])
				destheight = ord('z') if A[nx][ny] == 'E' else ord(A[nx][ny])
				# print("got here", x, y, nx, ny)
				if originheight + 1 >= destheight and d + 1 < best[nx][ny]:
					best[nx][ny] = d + 1
					heapq.heappush(q, (d + 1, nx, ny))
	# print(best)
	print(best[ex][ey])

def solve(s):
	solve1(s)
	solve2(s)
print("Sample:")
solve(
'''
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
)


print("\nActual:")
solve(
'''
abccccccccccccccccccccaaaaaaaacccccccccccccaacaaaaacccccccccccccccccccccaaaaaacccccaaaaaccccccccccccccccccccaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccccaaaa
abcccccccccccccccccccaaaaaaaaacccccccccccccaaaaaaaaccccccccccccccaacccccaaaaaaaaaaaaaaaaccccccccccccccccccccaaaccccccccccccccccccccccccaccaccccccccccccccccccccccccccccaaaaaa
abccccccccccccccccccaaaaaaaaaacccccaacccccccaaaaaccccccccccccccaaaaaacccaaaaaaaaaaaaaaaaccccccccccccccccccaacaaaaacccccccccccccccccccccaaaaccccccccccccccccccccccccccccaaaaaa
abccccccccccaaacaaacaaacaaacccccacaaaccccccccaaaaacccccccccccccaaaaaacaaaaaaaaaaaaaaaaaaccccccccccccccccccaaaaaaaaccccccccccccccccccccaaaaaccccccccaaaccccaaaccccccccccaaacaa
abccccccccaaaaaccaaaaaccaaaccccaaaaaaaacccccaaacaaccccccccccccccaaaaccaaaaaaaaccccaaaaaacccccccccccccccccccaaaaaccccccccccccccccccccccaaaaaacccccccaaaacccaaaccccccccccccccaa
abccccccccaaaaaaccaaaaaaaaaaaccaaaaaaaaccccccaacccccccccccccccccaaaacaaaacaaaacccccaaacccccccaacaaccccccccccaaaaacccaaccccccccccccccccaaaaaaccccccccaaaaaaaacccccccccccccccaa
abccccccccaaaaaaaaaaaaaaaaaaacccaaaaaaccccccccccccccccccccccccccaccaccccccaaaaaccccccccccccccaaaaacccccccccaaacaacaaaaaaccccccccccccccccaacccccccckkkkkkaaaaccccccccccccccccc
abccccccccaaaaacaaaaaccaaaaaaaacaaaaaccccccccccccccccccccccccccccccccccccccaaaccccccccccccccccaaaaacccccccccaaccccaaaaaaccccccccccccccccccccccccckkkkkkklaaccccccccaacccccccc
abccccccccaaaaacaacaaacaaaaaaaacaaaaaacccccccccccccccccccccaacccccccccccccccaaaccccccccccccccaaaaaacccccccccccccccaaaaaacccccccccccccccccccccccckkkkkkkklllccccccccccaaaacccc
abcaaccccccccccccccaaaccaaaaaaaccccaaccccccccccccccccccaaccaacccccccccccccccccccaacccccccccccaaaacccccccccccccccccaaaaacccccccaaaacccccccccccccckkkoppppllllllccccccccaaccccc
abcaacccccccccccccccccccaaaaaccccccccccccccccccccccccccaaaaaacccccccccccccccccaaaaaacccccccccccaaccccccccccccccccccaaaacccccccaaaaacccccccccccckkkooppppplllllllllccccdaccccc
abaaaccccccaaacccccccccaaaaaaccccccccaaaccccccccccccccccaaaaaaacccccccccccccccaaaaaacccccccccccccccccccccccccccccccccccccccccaaaaaaccccccccccccjkoooopuppplllllllmmmddddacccc
abaaaaaccccaaaaacccccccccccaaaaacccccaaaaccccccccccccccccaaaaaaccccccccccccccccaaaacccccccccccccccccaaaccccccccccccccccccccccaaaaaacccccccccccjjjooouuuuppppppqqmmmmmdddacccc
abaaaaacccaaaaaacccaacaaacccaaaaaacccaaaacccccccccccccccaaaaaccccccccccaaccccccaaaaccccccaacccccacccaaccccccccccaacaaccccccccaaaaaacccaaaccccjjjjoouuuuuuppppqqqqqmmmdddacccc
abaaccacccaaaaaacccaaaaaacccaaaaaacccaaacccccccccccccccaaaaaaccccccccaaaaaaccccaccacccccaaaacccaaaaaaaccccccccccaaaaaccccccccccaacacccaaccccjjjjooouuuxuuupppqqqqqmmmdddccccc
abaaaccccccaaaaacccaaaaaacccaaaaaccccccccccccccccccccccccccaaccccccccaaaaaacccccccccccccaaaaccccaaaaaaaaccccccccaaaaaaccccccccccccaaaaaaacjjjjjoooouuxxxuuvvvvvvqqqmmdddccccc
abaaaccccccaacaacccaaaaaaacccaaaaacccccccccccccccaaacccccccccccccccccaaaaaccccaaacccccccaaaaccccaaaaaaaaacccccccaaaaaaccccccccccccaaaaaacjjjjjoooouuuxxxuuvvvvvvqqqmmdddccccc
abccccccccccccccccaaaaaaaacccaaaaacccccccccccccccaaaccccccccccccccccccaaaaacccaaacacccccccccccccaaaaaaaaacccccccaaaaaccccccaacccccaaaaaaajjjnoooottuuxxxxvyyyvvvqqmmmdddccccc
abccccccccccccccccaaaaaaaacccccccccccccccccaaaaaaaaaccaaccccccccccccccaaaaacaacaaaaaccccccccccccaaaaaaaaccccccccccaaacccccaaaaccccaaaaaajjjnnnntttttxxxxyyyyyvvvqqmmmdddccccc
abccccccaaaccccccccccaaacccaaccccccccccccccaaaaaaaaaaaaaaaccccccccaaacccccccaaaaaaaacccccccccccaaaaaaaaccccccccccccaacccccaaaaacacaaaaaaiiinnntttxxxxxxxyyyyyvvqqqmmdddcccccc
SbccccccaaaaaccccccccaaccccaaaccccccccccccccaaaaaaaaaaaaaacccccccaaaaaaccccccaaaaaccccccccacccaaaccaaacccccccccaaacaaccaaaaaaaaaaaaaaaaaiiinnntttxxxEzzzzyyyvvqqqmmmeeecccccc
abcccccaaaaaacccccccccccaaaaaaaaccccccccccccaaaaaaaaaaaaaccccccccaaaaaacccccccaaaaacccccccaacaaaccccaaacccccccccaaaaaccaaaaaaaaaacaccaaaiiinnntttxxxxxyyyyyvvvqqqnnneeecccccc
abaacccaaaaaacccccccccccaaaaaaaaccccaaaccccaaaaaaaaaaaaaaacccccccaaaaaccccccccaacaaaaaccccaaaaacccccccccccccccccaaaaaaaccaaaaaacccccccaaiiinnnttttxxxxyyyyyyvvvrrnnneeecccccc
abaaaaaaaaaaaccccccccccccaaaaaaccccaaaacccaaaaaaaaaaaaacaaccccccccaaaaacccccccaaccccaaaacccaaaaaacaacaaccccccccaaaaaaaaccaaaaaaccccccccciiiinnnttttxxwyywyyyyvvrrrnneeecccccc
abaaaaacaacaaccccccccccccaaaaaaccccaaaacccaaacaaaacaaaccccccccccccaacaaccccaacccccaaaaaacaaaaaaaacaaaaacccccaaaaaaaaaaaccaaaaaacccccccccciiiinnnttttwwyywwywwwvrrrnneeecccccc
abaaaacccccccccccccccccccaaaaaacccccaaacccccccaaacccacaaccccccccccccccccccaaccccccaaaaaccaaaaaaaaaaaaaccccccaaaaaaaaacccaaaaaaaacccccccccciiinnnnntswwywwwwwwwwrrrnnneecccccc
abaaaaaccccccccccccccccccaacaaacccccccccccccccaacaaacaaacccccccccccccccaaaaacaaccccaaaaaccccaacccaaaaaacccccaaacaaaaaccccacccccccaaacccccciiiiinnmsswwwwwswwwwrrrrnnneecccccc
abaaaaaaccaaaccccccccccccccccccccccccccccccccccccaaaaaaaccccccccaaaccccaaaaaaaaccccaaccaccccaacccccaaaaccaaaaaaaaaaccccccccccccccaaaaacccccciihmmmsswwwwssrrrrrrrrnnneecccccc
abaaccaacaaaaccccccccccccccccccccccccccccccccccccaaaaaacccccccccaaaaaccccaaaaacccccccccccccccccccccacccccaaaaaaaaacccccccaaccaacaaaaacccccccchhhmmssswwsssrrrrrrrnnneeecccccc
abaacccccaaaacccccccccccccccccccccccccccccccccccccaaaaaaaacccccaaaaaacccaaaaacccccccccccccccccccccccccccccaaaaaaaccccccccaaaaaacaaaaacccccccchhhmmssssssslllllllnnnnfeecccccc
abccccccccaaacccccccccccccccaaccccccccccccccaaaccaaaaaaaaacccccaaaaaacccaacaaaccccccccccccccccccccccccaacccaaaaaaccccccccaaaaacccaaaaaccccccchhhmmmssssslllllllllnnfffeaacccc
abcccccccccccccccccccccccacaaaccccccccccccccaaaaaaaaaaaaaaccaaccaaaaaccccccaaccaacccccccccccccccccccccaaaccaaaaaaacccccccaaaaaaccaaccccccccccchhhmmmmsmllllllllllfffffaaacccc
abccccccccccccccccccccccaaaaaaaaccccccccccccaaaaaaacaaacaaaaaaccaaaaccccccccccaaaacccccccccccccccccaaaaaaaaaaacaaaccccccaaaaaaaacccccccccccccchhhmmmmmmlllggfffffffffaacccccc
abccccccccccccccccccccccaaaaaaaaccccccccccccaaacccccaaacaaaaacccccccccccaaacccaaaacccccccccccccccccaaaaaaaaaacccccccccccaaaaaaaaccccccccccccccchhhmmmmmlggggffffffffaaacccccc
abccccccccccccccccaaaacccaaaaaacccccccccccccccccccccaaacaaaaaaccccccccccaaacccaaaaccccccacccccccccccaaaaaacccccccccccccccccaacccaaccccccccccccchhhhgmgggggggffaccccccaacccccc
abccccccccccccccccaaaacccaaaaacccccccccccccccccccccccccaaaaaaaacccccccccaaaaccaaacccccccaaacaaacccccaaaaaacccccccccccccccccaaccaaccccccccccccccchhhgggggggaaaaacccccccccccccc
abccccccccccccccccaaaacccaaaaaaccccccccccccccccccccccccaaaaaaaaccccccccccaaaaaaaaaccccccaaaaaaacccccaaaaaaccccccccccccccccccaaaaacaaccccccccccccchggggggaacccccccccccccccccca
abcccccccccccccccccaacccccccaaccccccccccccccccccccccccccccaacaccaaacccaacaaaaaaaacccccccaaaaaaccccccaaccaacaaaccacccccaaccccaaaaaaaaccccccccccccccccccaaaccccccccccccccccccca
abcccccaaccccccccccccccccaaccccccccaacccccccccaaacccccccccaacaaaaaacccaaacaaaaaacccccccaaaaaaacccccccccccccaaaaaacccaaaaccccccaaaaaccccaaacccccccccccccaaccccccccccccccaaaaaa
abccccaaaacccccccccccccccaaaacccaaaaccccccccccaaaacccccccccccaaaaaaccaaaaaaaaaacccccccaaaaaaaaaaccccccccccccaaaaacccaaaaaacccaaaaacccccaaaacccccccccccaaccccccccccccccccaaaaa
abccccaaaacccccccccccccaaaaaacccaaaaaaccccccccaaaaccccccccccaaaaaaaacaaaaaaaaaaaaaccccaaaaaaaaaaccccccccccaaaaaaaacccaaaaccccaacaaaccccaaaacccccccccccccccccccccccccccccaaaaa
'''
)
