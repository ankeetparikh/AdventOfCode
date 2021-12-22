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


class Node:
  def __init__(self, data, par=None):
    self.par = par
    self.left = None
    self.right = None
    self.data = data

# solution begins here 

def main(filename):
  with open(filename) as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s.append("".join(line.strip()))
    
    def p1():
      sp = s.index("")
      alg = "".join(s[:sp])
      a = s[(sp+1):]

      lit = set()
      n = len(a)
      for i in range(n):
        for j in range(n):
          if a[i][j] == '#':
            lit.add((i, j))

      for iter in range(25):
        x = min(map(lambda e: e[0], lit)) - 2
        xx = max(map(lambda e: e[0], lit)) + 3
        y = min(map(lambda e: e[1], lit)) - 2
        yy = max(map(lambda e: e[1], lit)) + 3
        notlit = set()
        for i in range(x, xx):
          for j in range(y, yy):
            val = 0
            p = 8
            for ii in range(i - 1, i + 2):
              for jj in range(j - 1, j + 2):
                val += (2 ** p) * ((ii, jj) in lit)
                p -= 1
            if alg[val] == '.':
              notlit.add((i, j))

        x = min(map(lambda e: e[0], notlit)) - 2
        xx = max(map(lambda e: e[0], notlit)) + 3
        y = min(map(lambda e: e[1], notlit)) - 2
        yy = max(map(lambda e: e[1], notlit)) + 3
        lit = set()
        for i in range(x, xx):
          for j in range(y, yy):
            val = 0
            p = 8
            for ii in range(i - 1, i + 2):
              for jj in range(j - 1, j + 2):
                val += (2 ** p) * (0 if (ii, jj) in notlit else 1)
                p -= 1
            if alg[val] == '#':
              lit.add((i, j))
      print(len(lit))

      
      # print(len(lit))


    def p2():
      pass

    p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")