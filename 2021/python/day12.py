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
      s.append(line.strip())
    # print(s)
    def dfs(x, curpath, rep):
      if x == "start" and len(curpath) > 1:
        return 0
      if x == "end":
        # print(curpath)
        return 1
      res = 0
      for elem in s:
        a, b = elem.split("-")
        abig = a[0].isupper()
        bbig = b[0].isupper()
        if x == a:
          if bbig:
            res += dfs(b, curpath + [b], rep)
          else:
            if b not in curpath:
              res += dfs(b, curpath + [b], rep)
            elif rep == 0:
              res += dfs(b, curpath + [b], 1)
        if x == b:
          if abig:
            res += dfs(a, curpath + [a], rep)
          else:
            if a not in curpath:
              res += dfs(a, curpath + [a], rep)
            elif rep == 0:
              res += dfs(a, curpath + [a], 1)

      return res

    print(dfs("start", ["start"], 0))

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")