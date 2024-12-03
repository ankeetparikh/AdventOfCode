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
tot = 0
def main(filename):
  with open(filename) as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s.append(line.strip())
    s = s[0]
    print(s)
    he = {
      '0': '0000',
      '1': '0001',
      '2': '0010',
      '3': '0011',
      '4': '0100',
      '5': '0101',
      '6': '0110',
      '7': '0111',
      '8': '1000',
      '9': '1001',
      'A': '1010',
      'B': '1011',
      'C': '1100',
      'D': '1101',
      'E': '1110',
      'F': '1111'
    }

    def p1():
      b = ""
      for hval in s:
        b += he[hval]
      def get_value(typ, vals):

        typ = int(typ, 2)
        if typ == 0: return sum(vals)
        if typ == 1: return prod(vals)
        if typ == 2: return min(vals)
        if typ == 3: return max(vals)
        if typ == 5: return vals[0] > vals[1]
        if typ == 6: return vals[0] < vals[1]
        return vals[0] == vals[1]

      tot = 0
      def get(a):
        global tot
        ver = a[0:3]
        typ = a[3:6]
        tot += int(ver, 2)
        if typ == "100":
          i = 6
          rep = ""
          while True:
            rep += a[(i + 1):(i + 5)]
            if a[i] == '0':
              i += 5
              break
            i += 5
          # print("lit =", int(rep, 2))
          # print(tot)
          return (int(rep, 2), i)
          
        else:
          lenTyp = a[6]
          if lenTyp == "0":
            cnt = int(a[7:22], 2)
            # print("cnt =", cnt)
            subs = a[22:(22 + cnt)]
            # print("subs =", subs)
            ret = 0
            vals = []
            while ret < cnt:
              v = get(subs[ret:])
              vals.append(v[0])
              ret += v[1]
            return (get_value(typ, vals), 22 + cnt)
          else:
            cnt = int(a[7:18], 2)
            subs = a[18:]
            ret = 0
            vals = []
            for iter in range(cnt):
              v = get(subs[ret:])
              vals.append(v[0])
              ret += v[1]
            return (get_value(typ, vals), 18 + ret)
      
      # print(b)
      print(get(b))
      print(tot)

    def p2():
      pass

    p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  # main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")