from collections import defaultdict
import itertools
import functools
import operator
import json
import sys
import re
import math
import random

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
	file = open("in.txt", "r")
	lines = [line.strip() for line in file.readlines()]

	def eval_no_p(x):
		print("x = ", x)
		sys.stdout.flush()
		a = x.strip().split("*")
		def dosum(x):
			y = x.strip().split("+")
			return sum(int(x) for x in y)
		return prod(dosum(x) for x in a)
	

	def eval(x):
		while "(" in x:
			n = len(x)
			i = 0
			while x[i] != ')':
				i += 1
			j = i
			while x[j] != '(':
				j -= 1
			x = x[0:j] + str(eval_no_p(x[j+1:i])) + ("" if i + 1 >= n else x[i+1:])
		
		return eval_no_p(x)


	print(sum(eval( "(" + x + ")") for x in lines))

if __name__ == "__main__":
	main()