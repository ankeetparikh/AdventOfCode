import numpy as np

def solve1(s):
	s = s.strip().split("\n")
	a = s[0]


	g = {
		'E': 0,
		1: {'MG', 'MM'},
		2: {'CG', 'UG', 'RG', 'PG'},
		3: {'CM', 'UM', 'RM', 'PM'}
	}
	print(g)

	d = {}
	d[frozenset(g.items())] = 0




def solve2(s):
	return

def solve(s):
	solve1(s)
	solve2(s)
