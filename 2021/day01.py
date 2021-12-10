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

def di():
  return defaultdict(int)
def dl():
  return defaultdict(list)
def popcount(x):
	return x if x < 2 else (popcount(x // 2) + (x & 1))
def prod(x):
	return functools.reduce(operator.mul, x, 1)
def default():
	return 0
def defaultList():
	return []
def neighbors(x, y, diag = False):
	vectors = [
		[(1, 0), (-1, 0), (0, 1), (0, -1)],
		[(1, 1), (1, 0), (1, -1), (0, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
	][diag]
	print(vectors)
	return [(x + vectors[i][0], y + vectors[i][1]) for i in range(len(vectors))]

# solution begins here 

def main():
  with open("in.txt") as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s += list(map(int, line.split()))
    c = 0
    for i in range(3, len(s)):
      a = s[i - 3] + s[i - 2 ] + s[i - 1]
      b = a - s[i - 3] + s[i]
      if b > a:
        c +=1
    print(c)

if __name__ == "__main__":
  main()