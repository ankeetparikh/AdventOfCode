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
		[(1, 1), (1, 0), (1, -1), (0, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
	][diag]
	return [(x + vectors[i][0], y + vectors[i][1]) for i in range(len(vectors))]


# solution begins here 


def main(filename):
  with open(filename) as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s.append(list(map(int, line.strip())))
    
    n = len(s)
    m = len(s[0])

    def p1():
      risk = 0
      for i in range(n):
        for j in range(m):
          hi, tot = 0, 0
          for ii, jj in neighbors(i, j):
            if 0 <= ii < n and 0 <= jj < m:
              tot += 1
              if s[i][j] < s[ii][jj]:
                hi += 1
          if hi == tot:
            risk += 1 + s[i][j]
      print(risk)


    def p2():
      used = arr(n, m)

      def dfs(i, j):
        used[i][j] = 1
        sz = 1
        for ii, jj in neighbors(i, j):
          if 0 <= ii < n and 0 <= jj < m and s[ii][jj] != 9 and used[ii][jj] == 0:
            used[ii][jj] = 1
            sz += dfs(ii, jj)
        return sz

      sz = []
      for i in range(n):
        for j in range(m):
          if used[i][j] == 0 and s[i][j] < 9:
            sz.append(dfs(i, j))
      sz.sort()
      sz = sz[::-1]
      print(prod(sz[0:3]))

    p1()
    p2()
    


if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")