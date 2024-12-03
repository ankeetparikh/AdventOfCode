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
np.set_printoptions(threshold=sys.maxsize)

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
      s.append(line.strip())

    n, m = len(s), len(s[0])
    a = arr(n, m)
    for i in range(n):
      for j in range(m):
        a[i][j] = int(s[i][j])
    # print(a)
    def p1():
      dp = arr(n, m)
      
      for i in range(n):
        for j in range(m):
          if i == 0 and j == 0: dp[i][j] = a[i][j]    
          elif i == 0: dp[i][j] = dp[i][j - 1] + a[i][j]
          elif j == 0: dp[i][j] = dp[i - 1][j] + a[i][j]
          else:
            dp[i][j] = min(dp[i][j - 1] + a[i][j], dp[i - 1][j] + a[i][j])
            
      
      print(dp[n - 1][m - 1] - a[0][0])

    def p2():
      b = arr(5 * n, 5 * m)
      for i in range(n):
        for j in range(m):
          for x in range(5):
            for y in range(5):
              val = a[i][j] + x + y
              while val > 9:
                val -= 9
              b[x * n + i][y * m + j] = val

      dist = arr(5 * n, 5 * m)
      inf = 10**12
      for i in range(5 * n):
        for j in range(5 * m):
          dist[i][j] = inf

      dist[0][0] = b[0][0]
      h = [(dist[0][0], (0, 0))]
      heapq.heapify(h)
      
      while len(h) > 0:
        t = heapq.heappop(h)
        # print(t)
        i, j = t[1]
        for ii, jj in grid_nei(i, j, 5 * n, 5 * m):
          tmp = dist[i][j] + b[ii][jj]
          if tmp < dist[ii][jj]:
            dist[ii][jj] = tmp
            heapq.heappush(h, (tmp, (ii, jj)))         

      print(dist[5 * n - 1][5 * m - 1] - b[0][0])

    p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")