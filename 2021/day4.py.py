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
def enu(x):
  return enumerate(x)
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

def main(filename):
  with open(filename) as f:
    lines = f.readlines()
    s = [];
    for line in lines:
      s += [line.strip()]
    nums = list(map(int, s[0].split(",")))
    # print(nums)

    boards = []
    i = 2
    while i < len(s):
      strs = s[i:(i + 5)]
      board = []
      for row in strs:
        board.append(list(map(int, row.split())))

      boards.append(board)
      i += 6
    # print("boards: ", boards)

    def is_win(called, board):
      # print("board: ", board)
      for i in range(5):
        if 5 == sum(1 if board[i][j] in called else 0 for j in range(5)):
          return 1
        if 5 == sum(1 if board[j][i] in called else 0 for j in range(5)):
          return 1
      return 0

    def calc(called, board):
      unm = 0
      for row in b:
        for e in row:
          if e not in called:
            unm += e
      return unm * called[-1]


    cnt = 0
    B = len(boards)
    val = [-1] * B
    for i, x in enu(nums):
      called = nums[0:(i + 1)]
      for j, b in enu(boards):
        if is_win(called, b) and val[j] == -1:
          cnt += 1
          val[j] = calc(called, board)
          if cnt == B:
            print("result: ", val[j])



if __name__ == "__main__":
  print("~~~~~~~~~~~~~ Sample ~~~~~~~~~~~~~~")
  main("sample.txt")
  print("~~~~~~~~~~~~~ Actual ~~~~~~~~~~~~~~")
  main("in.txt")