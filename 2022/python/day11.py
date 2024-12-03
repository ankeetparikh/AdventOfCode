import fluentpy as _
import re
from collections import *
from itertools import *
from math import *
from functools import *
import string
import numpy as np

def solve1(s):
	x = list(
		_(s)
		.split("\n\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	M = len(x)
	monkeys = [{} for i in range(M)]
	for i, line in enumerate(x):
		line = line.strip().split('\n')
		monkeys[i]['items'] = deque(list(map(int, line[1].split(':')[1].split(','))))
		monkeys[i]['test'] = lambda old, expr=line[2].split('=')[1].strip(): eval(expr)
		monkeys[i]['mod'] = int(line[3].split()[-1])
		monkeys[i]['true'] = int(line[4].split()[-1])
		monkeys[i]['false'] = int(line[5].split()[-1])


	
	insp = [0 for i in range(M)]
	for r in range(20):
		for i in range(M):
			while len(monkeys[i]['items']):
				item = monkeys[i]['items'].popleft()
				newworry = monkeys[i]['test'](item) // 3
				if newworry % monkeys[i]['mod'] == 0:
					receiver = monkeys[i]['true']
				else:
					receiver = monkeys[i]['false']
				insp[i] += 1
				monkeys[receiver]['items'].append(newworry)

	insp = sorted(insp)[::-1]
	print(insp[0] * insp[1])

def solve2(s):
	x = list(
		_(s)
		.split("\n\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	M = len(x)
	monkeys = [{} for i in range(M)]
	for i, line in enumerate(x):
		line = line.strip().split('\n')
		monkeys[i]['items'] = list(map(int, line[1].split(':')[1].split(',')))
		monkeys[i]['test'] = lambda old, expr=line[2].split('=')[1].strip(): eval(expr)
		monkeys[i]['mod'] = int(line[3].split()[-1])
		monkeys[i]['true'] = int(line[4].split()[-1])
		monkeys[i]['false'] = int(line[5].split()[-1])

	LCM = 1
	for i in range(M):
		LCM *= monkeys[i]['mod']
	
	insp = [0 for i in range(M)]
	for r in range(10000):
		for i in range(M):
			for item in monkeys[i]['items']:
				newworry = monkeys[i]['test'](item) % LCM
				if newworry % monkeys[i]['mod'] == 0:
					receiver = monkeys[i]['true']
				else:
					receiver = monkeys[i]['false']
				insp[i] += 1
				monkeys[receiver]['items'].append(newworry)
			monkeys[i]['items'].clear()
	insp = sorted(insp)[::-1]
	print(insp[0] * insp[1])

def solve(s):
	solve1(s)
	solve2(s)
print("Sample:")
solve(
'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''
)


print("\nActual:")
solve(
'''
Monkey 0:
  Starting items: 83, 62, 93
  Operation: new = old * 17
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 1:
  Starting items: 90, 55
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 2:
  Starting items: 91, 78, 80, 97, 79, 88
  Operation: new = old + 3
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 64, 80, 83, 89, 59
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 4:
  Starting items: 98, 92, 99, 51
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 5:
  Starting items: 68, 57, 95, 85, 98, 75, 98, 75
  Operation: new = old + 2
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 6:
  Starting items: 74
  Operation: new = old + 4
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 2

Monkey 7:
  Starting items: 68, 64, 60, 68, 87, 80, 82
  Operation: new = old * 19
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 5
'''
)
