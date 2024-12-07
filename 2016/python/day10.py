from collections import defaultdict
from functools import reduce
import operator
def solve(s):
	s = s.strip().split("\n")
	z = defaultdict(set)
	cmds = []
	for inst in s:
		if "value" in inst:
			vals = inst.split()
			z[int(vals[5])].add(int(vals[1]))
		else:
			cmds.append(inst.split())
	outputs = defaultdict(set)
	while True:
		p = -1
		for k in z:
			if len(z[k]) == 2:
				p = k
				break
		if p == -1: break
		if set(z[p]) == set({17, 61}):
			print("Part 1:", p)
		u = list(z[p])
		lo = u[0]
		hi = u[1]
		if lo > hi: lo, hi = hi, lo
		for cmd in cmds:
			if cmd[1] == str(p):
				if cmd[5] == 'bot':
					z[int(cmd[6])].add(lo)
				if cmd[10] == 'bot':
					z[int(cmd[11])].add(hi)
				if cmd[5] == 'output':
					outputs[int(cmd[6])].add(lo)
				if cmd[10] == 'output':
					outputs[int(cmd[11])].add(hi)
		z[p] = set()

	print("Part 2:", reduce(operator.mul, outputs[0] | outputs[1] | outputs[2], 1))
		
with open('../inputs/day10input.txt') as f:
  s = f.read()
solve(s)