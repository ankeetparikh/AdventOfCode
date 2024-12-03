import fluentpy as _
import re
from collections import *
from itertools import *
from math import *
from functools import *
import string
import numpy as np
import heapq
import json
import networkx

def solve1(s):
	a = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	g = networkx.DiGraph()
	valve = {}
	p = defaultdict(int)
	ptr = 0
	for line in a:
		pattern = '^Valve ([A-Z]+) has flow rate=(\d+)'
		result = re.search(pattern, line)
		if 'valves' in line:
			to = line.split('valves')[1].split(",")
		else:
			to = [ line.split('valve')[1] ]
		u, amt = result.groups()
		amt = int(amt)
		valve[u] = amt
		p[u] = ptr
		ptr += 1
		for v in to:
			g.add_edge(u, v.strip())
	T = 30
	@lru_cache(maxsize=10**6)
	def rec(u, t, MASK):
		if t > T: return 0
		if MASK >> p[u] & 1:
			op = 0
		else:
			op = (T - t) * valve[u]
		b = op
		for _, v in g.edges(u):
			if op: b = max(b, op + rec(v, t + 2, MASK | (1 << p[u])))
			b = max(b, rec(v, t + 1, MASK))
		return b

	print(rec('AA', 1, 0))

def solve2(s):
	a = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	g = networkx.DiGraph()
	valve = {}
	p = defaultdict(int)
	ptr = 0
	for line in a:
		pattern = '^Valve ([A-Z]+) has flow rate=(\d+)'
		result = re.search(pattern, line)
		if 'valves' in line:
			to = line.split('valves')[1].split(",")
		else:
			to = [ line.split('valve')[1] ]
		u, amt = result.groups()
		amt = int(amt)
		valve[u] = amt
		p[u] = ptr
		ptr += 1
		for v in to:
			g.add_edge(u, v.strip())
	
	# h = networkx.DiGraph()
	# nodes = [u for u, amt in valve.items() if amt != 0] + ['AA']
	# for a in nodes:
	# 	for b in nodes:
	# 		d = networkx.shortest_path(g, a, b)
	# 		h.add_edge(a, b, weight=d)

	T = 26
	@lru_cache(maxsize=10**6)
	def rec(u, e, t, MASK):
		if t > T: return 0
		op = 0
		if MASK >> p[u] & 1:
			op += 0
		else:
			op += (T - t) * valve[u]

		if MASK >> p[e] & 1:
			op += 0
		else:
			op += (T - t) * valve[e]

		if op > 0 and u == e:
			op = (T - t) * valve[u]
		b = op
		for _, v in g.edges(u):
			for _, f in g.edges(e):
				b = max(b, rec(v, f, t + 1, MASK))
				if valve[u] and not (MASK >> p[u] & 1) :
					b = max(b, valve[u] * (T - t) + rec(u, f, t + 1, MASK | (1 << p[u])))
				if u != e and valve[e] and not (MASK >> p[e] & 1):
					b = max(b, valve[e] * (T - t) +  rec(v, e, t + 1, MASK | (1 << p[e])))
				if u != e and valve[u] and valve[e] and not (MASK >> p[u] & 1) and not (MASK >> p[e] & 1) :
					b = max(b, (valve[u] + valve[e]) * (T - t) + rec(u, e, t + 1, MASK | (1 << p[u]) | (1 << p[e])))
		return b

	print(rec('AA', 'AA', 1, 0))

def solve3(s):
	a = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	g = networkx.DiGraph()
	valve = {}
	has = []
	for line in a:
		pattern = '^Valve ([A-Z]+) has flow rate=(\d+)'
		result = re.search(pattern, line)
		if 'valves' in line:
			to = line.split('valves')[1].split(",")
		else:
			to = [ line.split('valve')[1] ]
		u, amt = result.groups()
		amt = int(amt)
		valve[u] = amt
		if amt:
			has.append(u)
		for v in to:
			g.add_edge(u, v.strip())
	
	h = networkx.DiGraph()
	nodes = [u for u, amt in valve.items() if amt != 0] + ['AA']
	print(nodes)
	for a in nodes:
		for b in nodes:
			if a != b:
				d = networkx.shortest_path(g, a, b)
				h.add_edge(a, b, weight=d)
	N = len(has)

	# generate compressed graph of nodes with non-zero valves
	# dp(time to get to next state for human, next state for human, time to get to next state for elephant, next state for elephant, things turned on)
	# 60 * 15 * 60 * 15 * (2 ** 15)

def solve(s):
	# solve1(s)
	solve3(s)
print("Sample:")
solve(
'''
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
'''
)


print("\nActual:")
solve(
'''
Valve EF has flow rate=22; tunnels lead to valves FK, HT, DE
Valve WT has flow rate=0; tunnels lead to valves XJ, XR
Valve RQ has flow rate=0; tunnels lead to valves VG, AV
Valve HF has flow rate=17; tunnels lead to valves EO, PQ, GX
Valve ZH has flow rate=0; tunnels lead to valves VG, RU
Valve AV has flow rate=0; tunnels lead to valves RQ, VQ
Valve AH has flow rate=12; tunnels lead to valves DF, FC, DE, MV, YC
Valve PQ has flow rate=0; tunnels lead to valves CF, HF
Valve DP has flow rate=18; tunnels lead to valves RD, OP, DR
Valve RU has flow rate=16; tunnels lead to valves ZH, VJ, AQ, SG
Valve AQ has flow rate=0; tunnels lead to valves RU, WE
Valve KO has flow rate=0; tunnels lead to valves VQ, HQ
Valve EY has flow rate=0; tunnels lead to valves WE, VQ
Valve RC has flow rate=14; tunnels lead to valves QK, BL, EO
Valve AA has flow rate=0; tunnels lead to valves XV, MS, BG, RT, HQ
Valve IH has flow rate=0; tunnels lead to valves VQ, VJ
Valve CK has flow rate=0; tunnels lead to valves SG, KG
Valve BG has flow rate=0; tunnels lead to valves DY, AA
Valve UJ has flow rate=0; tunnels lead to valves AF, OY
Valve HQ has flow rate=0; tunnels lead to valves AA, KO
Valve XV has flow rate=0; tunnels lead to valves AA, YL
Valve BL has flow rate=0; tunnels lead to valves DY, RC
Valve YL has flow rate=0; tunnels lead to valves WE, XV
Valve RT has flow rate=0; tunnels lead to valves VG, AA
Valve MV has flow rate=0; tunnels lead to valves AH, OM
Valve WE has flow rate=5; tunnels lead to valves AQ, YL, OM, ZU, EY
Valve HN has flow rate=0; tunnels lead to valves OP, XJ
Valve UR has flow rate=0; tunnels lead to valves NZ, OY
Valve FK has flow rate=0; tunnels lead to valves OY, EF
Valve GE has flow rate=0; tunnels lead to valves DF, XE
Valve GX has flow rate=0; tunnels lead to valves HF, DY
Valve YC has flow rate=0; tunnels lead to valves QC, AH
Valve XR has flow rate=0; tunnels lead to valves DY, WT
Valve MS has flow rate=0; tunnels lead to valves AA, DR
Valve EO has flow rate=0; tunnels lead to valves HF, RC
Valve VQ has flow rate=9; tunnels lead to valves NZ, KO, EY, AV, IH
Valve DY has flow rate=23; tunnels lead to valves XR, GX, BL, BG
Valve XJ has flow rate=24; tunnels lead to valves QK, HN, WT
Valve RD has flow rate=0; tunnels lead to valves VG, DP
Valve ZU has flow rate=0; tunnels lead to valves VG, WE
Valve AF has flow rate=0; tunnels lead to valves KG, UJ
Valve DR has flow rate=0; tunnels lead to valves MS, DP
Valve NZ has flow rate=0; tunnels lead to valves VQ, UR
Valve DE has flow rate=0; tunnels lead to valves EF, AH
Valve OP has flow rate=0; tunnels lead to valves DP, HN
Valve QK has flow rate=0; tunnels lead to valves XJ, RC
Valve CF has flow rate=20; tunnel leads to valve PQ
Valve FC has flow rate=0; tunnels lead to valves KH, AH
Valve KG has flow rate=25; tunnels lead to valves HT, AF, KH, CK
Valve XE has flow rate=11; tunnel leads to valve GE
Valve OY has flow rate=7; tunnels lead to valves FK, UJ, UR, QC
Valve OM has flow rate=0; tunnels lead to valves MV, WE
Valve QC has flow rate=0; tunnels lead to valves YC, OY
Valve DF has flow rate=0; tunnels lead to valves AH, GE
Valve KH has flow rate=0; tunnels lead to valves KG, FC
Valve SG has flow rate=0; tunnels lead to valves CK, RU
Valve VG has flow rate=3; tunnels lead to valves ZH, ZU, RQ, RD, RT
Valve HT has flow rate=0; tunnels lead to valves KG, EF
Valve VJ has flow rate=0; tunnels lead to valves IH, RU
'''
)
