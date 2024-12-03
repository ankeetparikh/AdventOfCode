import fluentpy as _
import re
from collections import *
from itertools import *
from math import *
from functools import *
import string
import numpy as np

def solve(s):
	x = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	vals = defaultdict(int)
	X = 1
	cyc = 1
	for line in x:
		a, *b = line.split()
		if a == 'addx':
			b = int(b[0])
			for i in range(2):
				vals[cyc + i] = X
			X += b
			vals[cyc + 2] = X
			cyc += 2
		else:
			vals[cyc] = X
			cyc += 1
	print(sum(vals[i] * i for i in [20, 60, 100, 140, 180, 220]))

	s = []

	for px in range(len(vals)):
		ch = '#' if px % 40 in range(vals[px + 1] - 1, vals[px + 1] + 2) else '.'
		s.append(ch)
	i = 0
	while i < len(s):
		print(''.join(s[i:i+40]))
		i += 40

print("Sample:")
solve(
'''
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''
)


print("\nActual:")
solve(
'''
addx 1
noop
addx 2
addx 5
addx 2
noop
noop
noop
addx 5
noop
noop
addx 1
addx 2
addx -5
addx 12
addx 1
addx 4
addx 2
noop
addx -1
addx 4
noop
noop
addx -37
addx 21
addx -13
addx -3
noop
addx 3
addx 2
addx 5
addx -2
addx 7
addx -2
addx 2
addx 11
addx -4
addx 3
noop
addx -18
addx 7
addx 14
addx 2
addx 5
addx -39
addx 1
addx 5
noop
noop
noop
addx 1
addx 4
noop
addx 12
addx 10
addx -17
addx 5
addx -17
addx 14
addx 6
noop
addx 3
addx 7
noop
noop
addx 2
addx 3
noop
addx -40
addx 40
addx -33
addx -2
noop
addx 3
addx 2
addx 5
addx -7
addx 8
noop
addx 6
addx 8
addx -11
addx 8
noop
addx -19
addx 27
noop
addx -2
addx 4
noop
addx -10
addx -27
noop
noop
addx 7
addx 4
addx -3
addx 2
addx 5
addx 2
addx -4
addx -3
addx 10
addx 15
addx -8
addx 2
addx 3
addx -2
addx 5
addx 2
addx 2
addx -39
addx 1
addx 3
addx 3
addx 3
noop
addx 2
addx 1
addx 4
addx -1
addx 2
addx 4
addx 1
noop
noop
addx 2
addx 5
addx 3
noop
noop
addx -27
addx 29
noop
addx 3
noop
noop
'''
)
