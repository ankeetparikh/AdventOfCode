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
    i = 0
    while s[i] != '': i += 1
    dots = []
    inst = s[i+1:]
    
    for j in range(i):
      x, y = s[j].split(",")
      x = int(x)
      y = int(y)
      dots.append((x, y))
      
    for elem in inst:
      o, v = elem.split()[2].split("=")
      v = int(v)
      ndots = []
      if o == "x":
        for x, y in dots:
          if x >= v:
            ndots.append((v - (x - v), y))
          else:
            ndots.append((x, y))
        dots = ndots
      else:
        for x, y in dots:
          if y >= v:
            ndots.append((x, v - (y - v)))
          else:
            ndots.append((x, y))
        dots = ndots
    a = arr(100, 100)
    for x, y in dots:
      a[x][y] += 1
    for i in range(100):
      for j in range(100):
        print("#" if a[99 - i][j] else ".", end = "")
      print()
    print(len(set(dots)))
    # print(dots)
    # print(inst)


    a = arr()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")