from collections import defaultdict
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

def di():
  return defaultdict(int)
def dl():
  return defaultdict(list)
def popcount(x):
	return x if x < 2 else (popcount(x // 2) + (x & 1))
def prod(x):
	return functools.reduce(operator.mul, x, 1)
def neighbors(x, y, diag = False):
	vectors = [
		[(1, 0), (-1, 0), (0, 1), (0, -1)],
		[(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
	][diag]
	print(vectors)
	return [(x + vectors[i][0], y + vectors[i][1]) for i in range(len(vectors))]

# solution begins here 

def main():
  with open("in.txt") as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s.append(line.strip())
    L = len(s[0])
    c = [0] * L
    for x in s:
      for i in range(L):
        if x[i] == "1":
          c[i] += 1

    def p1(a):
      u = ""
      for i in range(L):
        cnt = sum(1 if a[j][i] == '1' else 0 for j in range(len(a)))
        z = len(a) - cnt
        if cnt >= z:
          u += "1"
        else:
         u += "0"
      u = int(u, base=2)
      v = ((1 << L) - 1) ^ u
      return u * v

    def filter(a, i, b):
      aa = []
      for x in a:
        if x[i] == b:
          aa.append(x)
      return aa

    def o(a):
      for i in range(L):
        cnt = sum(1 if a[j][i] == '1' else 0 for j in range(len(a)))
        z = len(a) - cnt
        b = "1" if cnt >= z else "0"
        a = filter(a, i, b)
      return int(a[0], base=2)
    def co2(a):
      for i in range(L):
        if len(a) == 1:
          break
        cnt = sum(1 if a[j][i] == '1' else 0 for j in range(len(a)))
        z = len(a) - cnt
        b = "0" if z <= cnt else "1"
        a = filter(a, i, b)
      return int(a[0], base=2)


    print(p1(s))
    print(o(s) * co2(s))
    # u, v = '', ''
    # for i in range(L):
    #   if c[i] >= len(s) - c[i]:
    #     u += "1";
    #     v += "0";
    #   else:
    #     u += "0";
    #     v += "1";
    # print(int(u, base=2) * int(v, base=2) ) 

if __name__ == "__main__":
  main()