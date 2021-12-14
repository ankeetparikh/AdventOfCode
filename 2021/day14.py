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

    aa = ""
    ins = []
    for i, x in enu(s):
      if x == "":
        aa = s[0:i][0]
        ins = s[(i+1):]
        break
    rules = {}
    for elem in ins:
      x, y = elem.split("->")
      x = x.strip()
      y = y.strip()
      rules[x] = y
    def p1():
      a = aa
      for step in range(10):
        n = len(a)
        ne = []
        for i in range(n):
          ne.append(a[i])
          if i == n - 1: break
          pa = a[i:(i + 2)]
          if pa in rules:
            ne.append(rules[pa])

        a = "".join(ne)
        # print(a)

      a = [char for char in a]
      b = Counter(a)
      print(b.most_common()[0][1] - b.most_common()[-1][1]) 

    def p2():
      a = aa
      cnt = di()
      n = len(a)
      for i in range(n - 1):
        cnt[a[i:(i + 2)]] += 1
      for i in range(40):
        ncnt = di()
        for k, v in cnt.items():
          if k in rules:
            ch = rules[k]
            ncnt[k[0] + ch] += v
            ncnt[ch + k[1]] += v
          else:
            ncnt[k] += v
        cnt = ncnt
      # print(cnt)
      freq = di()
      for k, v in cnt.items():
        freq[k[0]] += v
        freq[k[1]] += v
      for k, v in freq.items():
        if v % 2 == 0:
          freq[k] //= 2
        else:
          freq[k] = (freq[k] + 1) // 2

      b = Counter(freq)
      # print(b)

      # b = Counter(cnt)
      print(b.most_common()[0][1] - b.most_common()[-1][1]) 


    p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")