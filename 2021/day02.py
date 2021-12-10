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
      s.append(list(line.split()))

    x, y, aim = 0, 0, 0
    for v, i in s:
      i = int(i)
      if v == "forward":
        x += i
        y += aim * i
      if v == "down":
        aim += i
        # y += i
      if v == "up":
        aim -= i
        # y -= i
    print(x * y)

if __name__ == "__main__":
  main()