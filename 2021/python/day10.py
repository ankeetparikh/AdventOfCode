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
	return [(x + vectors[i][0], y + vectors[i][1]) for i in range(len(vectors))]


# solution begins here 


def main(filename):
  with open(filename) as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s.append(line.strip())

    m = {
      ')': 3, ']': 57, '}': 1197, ">": 25137
    }
    c = {
      ')': 1, ']': 2, '}': 3, ">": 4
    }
    k = {
      "(": ")",
      "[": "]",
      "{": "}",
      "<": ">"
    }
    inv = {}
    for x, y in k.items():
      inv[y] = x

    def solve():
      badcost = 0
      sc = []
      for ind, x in enu(s):
        st = []
        bad = False
        for i in x:
          if i in k.keys():
            st.append(i)
          else:
            if st[-1] != inv[i]:
              badcost += m[i]
              
              bad = True
              break
            else:
              st = st[:len(st)-1]
        if not bad:
          r = []
          for i in st:
            r.append(k[i])
          r = r[::-1]
          tot = 0
          for i in r:
            tot = tot * 5 + c[i]
          sc.append(tot)
      sc.sort()
      print(badcost)
      print(sc[len(sc) // 2])


    solve()
    


if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")