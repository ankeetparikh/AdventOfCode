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
      s.append(list(map(int, line.split())))
    s = s[0]

    i = 0
    def get():
      nonlocal i
      i = i + 1
      if i > 100:
        i = 1
      return i

    def p1():
      t = 0
      pos = s.copy()
      pos[0] -= 1
      pos[1] -= 1
      tot = [0, 0]
      rcnt = 0
      while True:
        rcnt += 3
        roll = get() + get() + get()
        pos[t] += roll
        pos[t] %= 10
        tot[t] += pos[t] + 1
        if tot[t] >= 1000:
          break
        t = 1 - t
        
      print(rcnt * min(tot))

    def p2():
      # print(s)
      @functools.lru_cache(maxsize=100000)
      def dp(p0sc, p1sc, p0pos, p1pos, ne):
        if p0sc >= 21 or p1sc >= 21:
          return [0, 1] if ne == 0 else [1, 0]
        v = [0, 0]
        for x in itertools.product([1, 2, 3], repeat=3):
          tot = sum(x)
          if ne == 0:
            npos = (p0pos + tot) % 10
            y = dp(p0sc + npos + 1, p1sc, npos, p1pos, 1 - ne)
            v[0] += y[0]
            v[1] += y[1]
          else:
            npos = (p1pos + tot) % 10
            y = dp(p0sc, p1sc + npos + 1, p0pos, npos, 1 - ne)
            v[0] += y[0]
            v[1] += y[1]

        return v

      print(max(dp(0, 0, s[0] - 1, s[1] - 1, 0)))

    p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")