import numpy as np

def solve1(s):
	print(s)

def solve2(s):
	return

def solve(s):
	solve1(s)
	solve2(s)

with open('../inputs/day11input.txt') as f:
  s = f.read()
solve(s)