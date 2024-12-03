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
    for line in lines[0:2]:
      s.append(list(map(int, line.strip().split())))
    
    x, xx = s[0]
    y, yy = s[1]
    print(s)
    def p1():
      def go(du, dv):
        u, v = 0, 0
        yvals = []
        inT = False
        while True:
          u += du
          v += dv
          yvals.append(v)
          # print("pos=", u, v)
          if du > 0: du -= 1
          dv -= 1
          if x <= u <= xx and y <= v <= yy: 
            return True
          if v < y: break
       
        return False
      cnt = 0
      for du in range(1, xx + 1):
        for dv in range(-100, 200):
          cnt += go(du, dv)
      print(cnt)

    def p2():
      pass

    p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")