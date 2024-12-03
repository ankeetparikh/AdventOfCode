from collections import defaultdict, Counter
from cachetools import cached, LRUCache
import itertools
import functools
import operator
import json
import sys
import re
import math
import random
import time
import heapq
import numpy as np

# multidimensional integer array: arr(1), arr(2, 3)
def arr(*dims):
  return np.zeros(shape=(dims), dtype=int)
def di():
  return defaultdict(int)
def dl():
  return defaultdict(list)
def enu(x):
  return enumerate(x)
def popcount(x):
	return x if x < 2 else (popcount(x // 2) + (x & 1))
def prod(x):
	return functools.reduce(operator.mul, x, 1)
def neighbors(x, y, diag = False):
	vectors = [
		[(1, 0), (-1, 0), (0, 1), (0, -1)],
		[(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
	][diag]
	for i in range(len(vectors)):
		yield (x + vectors[i][0], y + vectors[i][1])
def grid_nei(x, y, n, m, diag=False):
	for xx, yy in neighbors(x, y, diag):
		if 0 <= xx < n and 0 <= yy < m:
			yield (xx, yy)


# solution begins here 


def main(filename):
  with open(filename) as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s.append(list(map(int, line.strip())))

    # this solution only works if number of iterations for part two is >= 100, which it is :)
    n, m = len(s), len(s[0])
    fl = 0
    L = 100
    p1, p2 = 0, 0
    for iter in range(L**L):
      for i in range(n):
        for j in range(m):
          s[i][j] += 1
      didFl = set()
      while True:
        has = False
        for i in range(n):
          for j in range(m):
            if s[i][j] > 9 and (i, j) not in didFl:
              has = True
              for ii, jj in grid_nei(i, j, n, m, diag=True):
                  s[ii][jj] += 1
              didFl.add((i, j))
        if not has:
          break
      if len(didFl) == n * m:
        p2 = iter + 1
        break
      for i, j in didFl:
        s[i][j] = 0
        if iter < L:
          p1 += 1
    print("Part 1:", p1)
    print("Part 2:", p2)

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")