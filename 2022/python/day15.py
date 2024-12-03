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

def solve1(Y, s):
	a = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	se = []
	be = []
	d = []
	MN, MX = 10**20, -10**20
	for line in a:
		pattern = '^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$'
		result = re.search(pattern, line)
		x, y, xx, yy = [int(u) for u in result.groups()]
		dist = abs(xx - x) + abs(yy - y)
		se.append((x, y))
		be.append((xx, yy))
		d.append(dist)
		MN = min(MN, x - dist - 10)
		MX = max(MX, x + dist + 10)
	# print(d)
	S = set(se)
	B = set(be)
	ct = 0
	for i in range(MN, MX):
		if (i, Y) in S or (i, Y) in B: continue
		if any(abs(i - x) + abs(Y - y) <= z for (x, y), z in zip(se, d)):
			ct += 1
	print(ct)
def solve2(M, Y, s):
	a = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)

	def union(intervals):
		if len(intervals) == 0: return []
		z = sorted(intervals)
		a, b = z[0]
		res = []
		for u, v in z[1:]:
			if b < u:
				res.append(a, b)
				a, b = u, v
			else:
				b = max(b, v)
		res.append((a, b))
		return res

	se = []
	be = []
	d = []
	MN, MX = 10**20, -10**20
	for line in a:
		pattern = '^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$'
		result = re.search(pattern, line)
		x, y, xx, yy = [int(u) for u in result.groups()]
		dist = abs(xx - x) + abs(yy - y)
		se.append((x, y))
		be.append((xx, yy))
		d.append(dist)
		MN = min(MN, x - dist - 10)
		MX = max(MX, x + dist + 10)

	S = set(se)
	B = set(be)
	for i in range(M):
		for j in range(M):
			if (i, j) in (S | B): continue
			if all(abs(i - x) + abs(j - y) > z for (x, y), z in zip(se, d)):
				print(i, j)

def solve(M, Y, s):
	solve1(Y, s)
	# solve2(M, Y, s)

print("Sample:")
solve(
20,
10,
'''
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
)


print("\nActual:")
solve(
4000000,
2000000,
'''
Sensor at x=391282, y=2038170: closest beacon is at x=-532461, y=2166525
Sensor at x=3042382, y=3783761: closest beacon is at x=3113582, y=3814857
Sensor at x=3444090, y=757238: closest beacon is at x=2930045, y=2000000
Sensor at x=971638, y=288172: closest beacon is at x=935006, y=638195
Sensor at x=2175844, y=1879176: closest beacon is at x=2930045, y=2000000
Sensor at x=3063103, y=3820576: closest beacon is at x=3113582, y=3814857
Sensor at x=2591294, y=3667337: closest beacon is at x=2768198, y=3762135
Sensor at x=2579773, y=3989626: closest beacon is at x=2768198, y=3762135
Sensor at x=2887876, y=2106773: closest beacon is at x=2930045, y=2000000
Sensor at x=2808659, y=3280271: closest beacon is at x=2768198, y=3762135
Sensor at x=2874212, y=3897058: closest beacon is at x=2768198, y=3762135
Sensor at x=720384, y=134640: closest beacon is at x=935006, y=638195
Sensor at x=489, y=1241813: closest beacon is at x=-532461, y=2166525
Sensor at x=120643, y=2878973: closest beacon is at x=227814, y=3107489
Sensor at x=3990734, y=2991891: closest beacon is at x=3924443, y=3039680
Sensor at x=1494086, y=3030634: closest beacon is at x=2537630, y=2793941
Sensor at x=1864417, y=360451: closest beacon is at x=935006, y=638195
Sensor at x=2974807, y=3732804: closest beacon is at x=3113582, y=3814857
Sensor at x=3273340, y=3998032: closest beacon is at x=3113582, y=3814857
Sensor at x=1468886, y=1597081: closest beacon is at x=935006, y=638195
Sensor at x=2083016, y=3743849: closest beacon is at x=2768198, y=3762135
Sensor at x=3387080, y=3393862: closest beacon is at x=3113582, y=3814857
Sensor at x=2959440, y=2052862: closest beacon is at x=2930045, y=2000000
Sensor at x=1180804, y=1112043: closest beacon is at x=935006, y=638195
Sensor at x=2829808, y=2206448: closest beacon is at x=2930045, y=2000000
Sensor at x=3999024, y=3114260: closest beacon is at x=3924443, y=3039680
Sensor at x=540955, y=3893312: closest beacon is at x=227814, y=3107489
Sensor at x=3669058, y=2350731: closest beacon is at x=3924443, y=3039680
Sensor at x=2915068, y=2754266: closest beacon is at x=2537630, y=2793941
Sensor at x=3507419, y=2838686: closest beacon is at x=3924443, y=3039680
Sensor at x=165939, y=498589: closest beacon is at x=935006, y=638195
Sensor at x=3917917, y=3792648: closest beacon is at x=3924443, y=3039680
Sensor at x=40698, y=3202257: closest beacon is at x=227814, y=3107489
Sensor at x=2619948, y=2439745: closest beacon is at x=2537630, y=2793941
'''
)
