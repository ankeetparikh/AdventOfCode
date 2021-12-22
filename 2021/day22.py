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
      s.append(line.strip())
    

    def p1():
      on = set()
      for line in s:
        f, cub = line.split()
        a = cub.split(",")
        c = []
        for aa in a:  
          rng = aa.split("=")[1].split("..")
          c.append([int(rng[0]), int(rng[-1])])
        
        for x in range(max(-50, c[0][0]), min(50, c[0][1]) + 1):
          for y in range(max(-50, c[1][0]), min(50, c[1][1]) + 1):
            for z in range(max(-50, c[2][0]), min(50, c[2][1]) + 1):
              if f == "on":
                on.add((x, y, z))
              else:
                on.discard((x, y, z))

      print(len(on))
      
    def p2():

      def size(cube):
        return prod(c[1] - c[0] + 1 for c in cube)
      def does_intersect(cuba, cubb):
        def interval_intersect(I, J):
          return max(I[0], J[0]) <= min(I[1], J[1])
        ax, ay, az = cuba
        bx, by, bz = cubb
        return interval_intersect(ax, bx) and interval_intersect(ay, by) and interval_intersect(az, bz)

      # returns [x, y] where x is cuboids in a that are not in b, and y is vice versa
      def sym_int(cuba, cubb):
        if not does_intersect(cuba, cubb):
          # print("doesnt intersect")
          return [[cuba], [cubb]]
        cubc = []
        for a, b in zip(cuba, cubb):
          cubc.append([max(a[0], b[0]), min(a[1], b[1])])
        # print("cubc = ", cubc)
        ret = [[], []]
        for x in [[cuba[0][0], cubc[0][0] - 1], [cubc[0][0], cubc[0][1]], [cubc[0][1] + 1, cuba[0][1]]]:
          for y in [[cuba[1][0], cubc[1][0] - 1], [cubc[1][0], cubc[1][1]], [cubc[1][1] + 1, cuba[1][1]]]:
            for z in [[cuba[2][0], cubc[2][0] - 1], [cubc[2][0], cubc[2][1]], [cubc[2][1] + 1, cuba[2][1]]]:
              if x[1] - x[0] + 1 <= 0: continue
              if y[1] - y[0] + 1 <= 0: continue
              if z[1] - z[0] + 1 <= 0: continue
              curcub = [x, y, z]
              # print("curcub = ", curcub)
              if not does_intersect(curcub, cubc):
                ret[0].append(curcub)
        for x in [[cubb[0][0], cubc[0][0] - 1], [cubc[0][0], cubc[0][1]], [cubc[0][1] + 1, cubb[0][1]]]:
          for y in [[cubb[1][0], cubc[1][0] - 1], [cubc[1][0], cubc[1][1]], [cubc[1][1] + 1, cubb[1][1]]]:
            for z in [[cubb[2][0], cubc[2][0] - 1], [cubc[2][0], cubc[2][1]], [cubc[2][1] + 1, cubb[2][1]]]:
              if x[1] - x[0] + 1 <= 0: continue
              if y[1] - y[0] + 1 <= 0: continue
              if z[1] - z[0] + 1 <= 0: continue
              curcub = [x, y, z]
              # print("curcub = ", curcub)
              if not does_intersect(curcub, cubc):
                ret[1].append(curcub)

        return ret
      
      f = []
      r = []
      for line in s:
        ff, cub = line.split()
        a = cub.split(",")
        c = []
        for aa in a:  
          rng = aa.split("=")[1].split("..")
          c.append([int(rng[0]), int(rng[-1])])
        r.append(c)
        f.append(ff == "on")

      cubes = []
      for op, cube in zip(f, r):
        n = len(cubes)
        cur = [cube]
        if op:
          for i in range(n):
            ncur = []
            for curcub in cur:
              ncur += sym_int(cubes[i], curcub)[1]
            cur = ncur
          cubes += cur
        else:
          n = len(cubes)
          ncubes = []
          for i in range(n):
            for x in sym_int(cubes[i], cube)[0]:
              ncubes.append(x)
          cubes = ncubes

      print(len(cubes))
      print(sum(size(cube) for cube in cubes))
    # p1()
    p2()

if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")