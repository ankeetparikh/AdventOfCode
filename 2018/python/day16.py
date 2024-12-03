import re
import numpy as np

def solve(raw_inp):

	ins = {
		'addr': lambda r, a, b: r[a] + r[b],
		'addi': lambda r, a, b: r[a] + b,

		'mulr': lambda r, a, b: r[a] * r[b],
		'muli': lambda r, a, b: r[a] * b,

		'banr': lambda r, a, b: r[a] & r[b],
		'bani': lambda r, a, b: r[a] & b,

		'borr': lambda r, a, b: r[a] | r[b],
		'bori': lambda r, a, b: r[a] | b,

		'setr': lambda r, a, b: r[a],
		'seti': lambda r, a, b: a,

		'gtir': lambda r, a, b: int(a > r[b]),
		'gtri': lambda r, a, b: int(r[a] > b),
		'gtrr': lambda r, a, b: int(r[a] > r[b]),

		'eqir': lambda r, a, b: int(a == r[b]),
		'eqri': lambda r, a, b: int(r[a] == b),
		'eqrr': lambda r, a, b: int(r[a] == r[b]),
	}
	def apply(r, f, a, b, c):
		r = r.copy()
		r[c] = f(r, a, b)
		return r
	test_part, ins_part = raw_inp.strip().split("\n\n\n")
	tests = test_part.split("\n\n")
	tests = [[[int(x) for x in re.findall("-?\d+", line)] for line in test.split("\n")] for test in tests]
	p1 = 0
	for r1, (opc, a, b, c), r2 in tests:
		cnt = sum(apply(r1, f, a, b, c) == r2 for ins_name, f in ins.items())
		p1 += cnt >= 3
	print("Part 1:", p1)

	N = len(ins)

	op_cnt = np.zeros(N) # frequency of each opcode in tests
	matches = np.zeros((N, N)) # matches[i][j] = number of times instruction i accords with opcode j
	for r1, (opc, a, b, c), r2 in tests:
		op_cnt[opc] += 1
		for ins_ind, (opname, f) in enumerate(ins.items()):
			if apply(r1, f, a, b, c) == r2:
				matches[ins_ind][opc] += 1

	# run unique perfect matching algo
	# instruction i must accord with all occurrences of opcode j
	ins_ind_to_ins = { ins_ind: instr for ins_ind, (ins_name, instr) in enumerate(ins.items())}
	op_ind_to_ins_ind = {}
	for k in range(N):
		for i in range(N):
			can = [j for j in range(N) if matches[i][j] == op_cnt[j]]
			if len(can) == 1:
				j = can[0]
				for p in range(N): matches[p][j] = matches[i][p] = -1
				op_ind_to_ins_ind[j] = i
	# execute instructions
	reg = [0] * 4
	for ins_line in ins_part.strip().split('\n'):
		op_ind, a, b, c = [int(x) for x in ins_line.split()]
		f = ins_ind_to_ins[op_ind_to_ins_ind[op_ind]]
		reg = apply(reg, f, a, b, c)
	print("Part 2:", reg[0])
solve(
'''
Before: [2, 1, 1, 0]
10 1 3 1
After:  [2, 1, 1, 0]

Before: [1, 1, 3, 3]
6 1 0 0
After:  [1, 1, 3, 3]

Before: [2, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 2, 2, 3]
1 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 2, 3, 2]
12 0 2 3
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 1]
13 3 3 2
After:  [1, 1, 0, 1]

Before: [1, 1, 2, 1]
15 3 2 3
After:  [1, 1, 2, 1]

Before: [2, 1, 1, 0]
8 2 1 2
After:  [2, 1, 0, 0]

Before: [1, 1, 1, 2]
8 2 1 3
After:  [1, 1, 1, 0]

Before: [0, 3, 1, 1]
0 0 0 2
After:  [0, 3, 0, 1]

Before: [1, 1, 1, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [3, 1, 2, 0]
10 1 3 1
After:  [3, 1, 2, 0]

Before: [1, 2, 2, 1]
1 0 2 2
After:  [1, 2, 0, 1]

Before: [2, 1, 3, 3]
12 0 2 3
After:  [2, 1, 3, 2]

Before: [0, 1, 1, 3]
7 2 3 1
After:  [0, 0, 1, 3]

Before: [1, 1, 2, 3]
2 1 2 2
After:  [1, 1, 0, 3]

Before: [3, 1, 3, 2]
14 1 3 2
After:  [3, 1, 0, 2]

Before: [1, 1, 1, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 3, 0, 3]
9 0 2 0
After:  [0, 3, 0, 3]

Before: [0, 3, 2, 0]
3 2 1 1
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 0]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 3, 0, 0]
0 0 0 3
After:  [0, 3, 0, 0]

Before: [2, 1, 2, 3]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [1, 1, 3, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 1, 2, 1]
15 3 2 3
After:  [0, 1, 2, 1]

Before: [1, 1, 2, 2]
2 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 0]
1 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 1, 0, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [2, 2, 3, 2]
12 3 2 0
After:  [2, 2, 3, 2]

Before: [1, 0, 2, 2]
11 2 2 2
After:  [1, 0, 2, 2]

Before: [2, 2, 0, 3]
7 1 3 3
After:  [2, 2, 0, 0]

Before: [1, 1, 3, 1]
6 1 0 0
After:  [1, 1, 3, 1]

Before: [2, 1, 2, 1]
9 1 3 1
After:  [2, 1, 2, 1]

Before: [2, 1, 1, 0]
4 0 1 3
After:  [2, 1, 1, 1]

Before: [2, 0, 0, 3]
8 0 1 1
After:  [2, 1, 0, 3]

Before: [0, 1, 2, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [2, 1, 3, 2]
12 3 2 1
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 1]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [0, 0, 2, 0]
0 0 0 0
After:  [0, 0, 2, 0]

Before: [1, 1, 2, 1]
1 0 2 2
After:  [1, 1, 0, 1]

Before: [0, 2, 2, 1]
0 0 0 1
After:  [0, 0, 2, 1]

Before: [3, 2, 0, 3]
8 0 2 3
After:  [3, 2, 0, 1]

Before: [3, 1, 2, 1]
2 1 2 1
After:  [3, 0, 2, 1]

Before: [3, 1, 0, 2]
14 1 3 0
After:  [0, 1, 0, 2]

Before: [3, 2, 2, 0]
11 2 2 3
After:  [3, 2, 2, 2]

Before: [0, 2, 2, 2]
0 0 0 2
After:  [0, 2, 0, 2]

Before: [1, 3, 2, 3]
11 2 2 3
After:  [1, 3, 2, 2]

Before: [2, 0, 2, 1]
15 3 2 3
After:  [2, 0, 2, 1]

Before: [0, 3, 0, 3]
0 0 0 2
After:  [0, 3, 0, 3]

Before: [1, 1, 2, 2]
1 0 2 0
After:  [0, 1, 2, 2]

Before: [1, 2, 3, 2]
12 1 2 3
After:  [1, 2, 3, 2]

Before: [3, 1, 1, 3]
5 3 0 2
After:  [3, 1, 1, 3]

Before: [0, 1, 1, 2]
0 0 0 2
After:  [0, 1, 0, 2]

Before: [0, 1, 2, 1]
9 1 3 3
After:  [0, 1, 2, 1]

Before: [0, 1, 2, 3]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 2]
14 1 3 2
After:  [3, 1, 0, 2]

Before: [2, 3, 3, 0]
3 0 1 3
After:  [2, 3, 3, 1]

Before: [3, 3, 2, 3]
5 3 0 1
After:  [3, 1, 2, 3]

Before: [2, 1, 2, 1]
13 3 3 3
After:  [2, 1, 2, 0]

Before: [1, 1, 2, 1]
8 3 1 3
After:  [1, 1, 2, 0]

Before: [1, 2, 0, 0]
9 0 2 0
After:  [0, 2, 0, 0]

Before: [2, 1, 1, 0]
10 1 3 3
After:  [2, 1, 1, 1]

Before: [3, 1, 1, 2]
14 1 3 3
After:  [3, 1, 1, 0]

Before: [1, 2, 3, 2]
12 3 2 3
After:  [1, 2, 3, 2]

Before: [3, 1, 1, 3]
7 2 3 2
After:  [3, 1, 0, 3]

Before: [1, 2, 0, 0]
9 0 2 1
After:  [1, 0, 0, 0]

Before: [1, 2, 3, 3]
12 1 2 2
After:  [1, 2, 2, 3]

Before: [1, 1, 2, 2]
11 2 2 0
After:  [2, 1, 2, 2]

Before: [1, 1, 0, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 1, 1, 1]
6 1 0 0
After:  [1, 1, 1, 1]

Before: [3, 1, 1, 3]
5 3 0 0
After:  [1, 1, 1, 3]

Before: [2, 1, 1, 3]
4 0 1 0
After:  [1, 1, 1, 3]

Before: [2, 1, 2, 2]
14 1 3 2
After:  [2, 1, 0, 2]

Before: [0, 1, 3, 1]
9 1 3 3
After:  [0, 1, 3, 1]

Before: [2, 1, 1, 1]
9 1 3 2
After:  [2, 1, 1, 1]

Before: [1, 1, 3, 3]
6 1 0 2
After:  [1, 1, 1, 3]

Before: [1, 3, 2, 1]
15 3 2 2
After:  [1, 3, 1, 1]

Before: [2, 3, 2, 1]
15 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 2, 3, 3]
12 1 2 3
After:  [3, 2, 3, 2]

Before: [0, 1, 3, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [0, 0, 3, 2]
0 0 0 3
After:  [0, 0, 3, 0]

Before: [0, 1, 0, 1]
13 3 3 1
After:  [0, 0, 0, 1]

Before: [0, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [2, 2, 3, 0]
12 0 2 3
After:  [2, 2, 3, 2]

Before: [0, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [3, 0, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [3, 3, 2, 1]
4 0 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 1, 2]
4 0 1 2
After:  [2, 1, 1, 2]

Before: [2, 1, 3, 2]
14 1 3 3
After:  [2, 1, 3, 0]

Before: [0, 2, 2, 1]
15 3 2 2
After:  [0, 2, 1, 1]

Before: [2, 1, 3, 1]
5 2 3 3
After:  [2, 1, 3, 0]

Before: [3, 1, 0, 1]
9 1 3 1
After:  [3, 1, 0, 1]

Before: [2, 1, 2, 2]
14 1 3 1
After:  [2, 0, 2, 2]

Before: [0, 1, 0, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [1, 1, 2, 1]
6 1 0 0
After:  [1, 1, 2, 1]

Before: [1, 0, 0, 1]
9 0 2 0
After:  [0, 0, 0, 1]

Before: [1, 1, 2, 1]
13 3 3 0
After:  [0, 1, 2, 1]

Before: [3, 1, 1, 1]
9 1 3 2
After:  [3, 1, 1, 1]

Before: [0, 1, 1, 1]
9 1 3 2
After:  [0, 1, 1, 1]

Before: [2, 0, 0, 2]
8 0 1 3
After:  [2, 0, 0, 1]

Before: [1, 0, 2, 2]
1 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 2]
2 1 2 1
After:  [1, 0, 2, 2]

Before: [3, 3, 2, 3]
5 3 0 3
After:  [3, 3, 2, 1]

Before: [3, 1, 0, 2]
14 1 3 1
After:  [3, 0, 0, 2]

Before: [2, 1, 3, 3]
8 2 0 2
After:  [2, 1, 1, 3]

Before: [0, 1, 2, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [3, 2, 2, 1]
15 3 2 3
After:  [3, 2, 2, 1]

Before: [2, 0, 1, 2]
8 0 1 0
After:  [1, 0, 1, 2]

Before: [2, 3, 0, 1]
13 3 3 1
After:  [2, 0, 0, 1]

Before: [2, 1, 3, 1]
5 2 3 2
After:  [2, 1, 0, 1]

Before: [0, 1, 2, 1]
2 1 2 2
After:  [0, 1, 0, 1]

Before: [2, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [2, 1, 1, 2]
4 0 1 3
After:  [2, 1, 1, 1]

Before: [2, 1, 0, 2]
14 1 3 3
After:  [2, 1, 0, 0]

Before: [2, 1, 0, 3]
7 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 3, 1, 1]
13 2 3 1
After:  [1, 0, 1, 1]

Before: [0, 2, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 3, 1, 1]
13 2 3 3
After:  [0, 3, 1, 0]

Before: [0, 2, 3, 2]
12 3 2 3
After:  [0, 2, 3, 2]

Before: [1, 3, 2, 0]
1 0 2 2
After:  [1, 3, 0, 0]

Before: [2, 0, 2, 2]
11 2 2 3
After:  [2, 0, 2, 2]

Before: [1, 0, 0, 2]
9 0 2 2
After:  [1, 0, 0, 2]

Before: [1, 1, 2, 1]
2 1 2 1
After:  [1, 0, 2, 1]

Before: [3, 2, 2, 2]
3 2 0 0
After:  [1, 2, 2, 2]

Before: [1, 1, 3, 2]
6 1 0 1
After:  [1, 1, 3, 2]

Before: [1, 1, 2, 0]
6 1 0 0
After:  [1, 1, 2, 0]

Before: [1, 1, 0, 2]
13 3 3 3
After:  [1, 1, 0, 0]

Before: [0, 3, 1, 1]
13 2 3 0
After:  [0, 3, 1, 1]

Before: [0, 2, 3, 1]
0 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 1, 2, 0]
10 1 3 3
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 2]
5 2 1 0
After:  [1, 2, 2, 2]

Before: [1, 1, 0, 2]
6 1 0 1
After:  [1, 1, 0, 2]

Before: [1, 0, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [0, 2, 2, 2]
5 2 1 0
After:  [1, 2, 2, 2]

Before: [2, 0, 3, 2]
12 3 2 1
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 2]
14 1 3 1
After:  [1, 0, 0, 2]

Before: [2, 3, 3, 1]
3 0 1 3
After:  [2, 3, 3, 1]

Before: [3, 0, 2, 1]
15 3 2 2
After:  [3, 0, 1, 1]

Before: [3, 1, 2, 2]
14 1 3 3
After:  [3, 1, 2, 0]

Before: [1, 0, 2, 3]
1 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 2, 0, 1]
0 0 0 1
After:  [0, 0, 0, 1]

Before: [3, 1, 0, 1]
9 1 3 3
After:  [3, 1, 0, 1]

Before: [1, 1, 3, 2]
14 1 3 1
After:  [1, 0, 3, 2]

Before: [2, 1, 1, 0]
4 0 1 1
After:  [2, 1, 1, 0]

Before: [2, 1, 1, 1]
8 3 1 3
After:  [2, 1, 1, 0]

Before: [0, 1, 1, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [1, 0, 2, 1]
1 0 2 2
After:  [1, 0, 0, 1]

Before: [1, 2, 2, 3]
11 2 2 1
After:  [1, 2, 2, 3]

Before: [3, 1, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [0, 0, 1, 0]
0 0 0 0
After:  [0, 0, 1, 0]

Before: [0, 2, 3, 3]
7 1 3 3
After:  [0, 2, 3, 0]

Before: [3, 1, 2, 1]
15 3 2 3
After:  [3, 1, 2, 1]

Before: [3, 1, 3, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [1, 1, 2, 0]
10 1 3 3
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
2 1 2 1
After:  [2, 0, 2, 1]

Before: [1, 1, 1, 1]
13 3 3 3
After:  [1, 1, 1, 0]

Before: [2, 1, 3, 1]
4 0 1 0
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 1]
8 2 1 3
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 3]
7 2 3 2
After:  [1, 1, 0, 3]

Before: [3, 2, 2, 2]
13 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 3, 3, 2]
13 3 3 0
After:  [0, 3, 3, 2]

Before: [0, 3, 2, 1]
15 3 2 2
After:  [0, 3, 1, 1]

Before: [1, 2, 2, 2]
1 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 1, 2, 1]
4 0 2 3
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 1]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 3]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 1, 2]
6 1 0 1
After:  [1, 1, 1, 2]

Before: [2, 3, 3, 3]
3 0 1 0
After:  [1, 3, 3, 3]

Before: [3, 2, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [3, 1, 3, 3]
7 1 3 0
After:  [0, 1, 3, 3]

Before: [2, 3, 3, 1]
3 0 1 0
After:  [1, 3, 3, 1]

Before: [0, 1, 3, 0]
10 1 3 3
After:  [0, 1, 3, 1]

Before: [3, 1, 1, 0]
10 1 3 2
After:  [3, 1, 1, 0]

Before: [2, 2, 2, 0]
5 2 1 2
After:  [2, 2, 1, 0]

Before: [1, 1, 0, 0]
9 0 2 2
After:  [1, 1, 0, 0]

Before: [2, 3, 3, 0]
3 0 1 1
After:  [2, 1, 3, 0]

Before: [2, 1, 3, 2]
14 1 3 0
After:  [0, 1, 3, 2]

Before: [0, 1, 2, 2]
0 0 0 0
After:  [0, 1, 2, 2]

Before: [2, 0, 3, 0]
12 0 2 0
After:  [2, 0, 3, 0]

Before: [1, 1, 0, 0]
10 1 3 2
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 2]
14 1 3 1
After:  [1, 0, 1, 2]

Before: [2, 1, 2, 3]
2 1 2 1
After:  [2, 0, 2, 3]

Before: [2, 3, 1, 0]
3 0 1 0
After:  [1, 3, 1, 0]

Before: [0, 3, 1, 3]
7 2 3 2
After:  [0, 3, 0, 3]

Before: [0, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 2]
11 2 2 2
After:  [3, 3, 2, 2]

Before: [0, 1, 3, 1]
0 0 0 2
After:  [0, 1, 0, 1]

Before: [3, 2, 0, 3]
5 3 0 1
After:  [3, 1, 0, 3]

Before: [0, 3, 2, 2]
3 2 1 0
After:  [1, 3, 2, 2]

Before: [1, 1, 3, 1]
6 1 0 1
After:  [1, 1, 3, 1]

Before: [2, 2, 2, 1]
15 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 2, 0]
10 1 3 0
After:  [1, 1, 2, 0]

Before: [1, 1, 1, 3]
6 1 0 2
After:  [1, 1, 1, 3]

Before: [2, 0, 3, 3]
8 0 1 3
After:  [2, 0, 3, 1]

Before: [3, 1, 3, 2]
13 3 3 3
After:  [3, 1, 3, 0]

Before: [3, 2, 2, 2]
4 0 2 2
After:  [3, 2, 1, 2]

Before: [1, 1, 1, 0]
8 2 1 2
After:  [1, 1, 0, 0]

Before: [1, 0, 2, 1]
1 0 2 0
After:  [0, 0, 2, 1]

Before: [2, 3, 2, 1]
13 3 3 0
After:  [0, 3, 2, 1]

Before: [3, 0, 2, 3]
4 0 2 2
After:  [3, 0, 1, 3]

Before: [2, 1, 0, 1]
9 1 3 0
After:  [1, 1, 0, 1]

Before: [3, 2, 2, 1]
15 3 2 2
After:  [3, 2, 1, 1]

Before: [3, 1, 2, 1]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 1, 0, 0]
6 1 0 0
After:  [1, 1, 0, 0]

Before: [1, 0, 3, 2]
13 3 3 0
After:  [0, 0, 3, 2]

Before: [0, 2, 2, 2]
5 2 1 3
After:  [0, 2, 2, 1]

Before: [2, 3, 3, 2]
12 0 2 3
After:  [2, 3, 3, 2]

Before: [0, 2, 1, 1]
0 0 0 0
After:  [0, 2, 1, 1]

Before: [3, 0, 2, 1]
11 2 2 3
After:  [3, 0, 2, 2]

Before: [3, 2, 2, 1]
4 0 2 3
After:  [3, 2, 2, 1]

Before: [3, 1, 0, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [1, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [0, 0, 1, 3]
7 2 3 0
After:  [0, 0, 1, 3]

Before: [0, 1, 3, 1]
8 3 1 3
After:  [0, 1, 3, 0]

Before: [2, 1, 1, 1]
4 0 1 2
After:  [2, 1, 1, 1]

Before: [1, 1, 0, 0]
10 1 3 0
After:  [1, 1, 0, 0]

Before: [0, 1, 3, 2]
13 3 3 3
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 0]
1 0 2 0
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 0]
2 1 2 1
After:  [3, 0, 2, 0]

Before: [0, 1, 1, 3]
7 2 3 3
After:  [0, 1, 1, 0]

Before: [0, 2, 3, 3]
12 1 2 0
After:  [2, 2, 3, 3]

Before: [2, 1, 1, 1]
8 3 1 0
After:  [0, 1, 1, 1]

Before: [0, 1, 1, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 1]
9 1 3 1
After:  [3, 1, 2, 1]

Before: [1, 2, 3, 2]
12 1 2 2
After:  [1, 2, 2, 2]

Before: [2, 3, 2, 2]
3 0 1 0
After:  [1, 3, 2, 2]

Before: [1, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [3, 2, 2, 2]
4 0 2 0
After:  [1, 2, 2, 2]

Before: [3, 1, 0, 2]
14 1 3 3
After:  [3, 1, 0, 0]

Before: [0, 3, 3, 2]
12 3 2 3
After:  [0, 3, 3, 2]

Before: [3, 3, 0, 0]
8 0 2 1
After:  [3, 1, 0, 0]

Before: [3, 0, 2, 0]
4 0 2 3
After:  [3, 0, 2, 1]

Before: [0, 3, 2, 1]
3 2 1 1
After:  [0, 1, 2, 1]

Before: [3, 0, 2, 3]
4 0 2 0
After:  [1, 0, 2, 3]

Before: [0, 1, 0, 0]
10 1 3 1
After:  [0, 1, 0, 0]

Before: [3, 3, 3, 3]
5 3 2 1
After:  [3, 1, 3, 3]

Before: [1, 2, 2, 0]
1 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 3, 1, 2]
0 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 3, 2, 3]
3 2 1 1
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 2]
14 1 3 0
After:  [0, 1, 3, 2]

Before: [3, 1, 1, 3]
7 1 3 3
After:  [3, 1, 1, 0]

Before: [2, 2, 2, 2]
13 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 1, 3, 3]
6 1 0 1
After:  [1, 1, 3, 3]

Before: [1, 1, 2, 0]
6 1 0 3
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 1]
3 2 0 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [0, 3, 3, 1]
13 3 3 1
After:  [0, 0, 3, 1]

Before: [1, 2, 2, 0]
1 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 2, 2, 0]
4 0 2 0
After:  [1, 2, 2, 0]

Before: [3, 1, 1, 3]
7 1 3 1
After:  [3, 0, 1, 3]

Before: [2, 2, 2, 3]
7 2 3 2
After:  [2, 2, 0, 3]

Before: [2, 1, 2, 2]
2 1 2 2
After:  [2, 1, 0, 2]

Before: [2, 0, 0, 3]
11 3 3 2
After:  [2, 0, 3, 3]

Before: [1, 1, 2, 1]
1 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 3, 3, 3]
0 0 0 3
After:  [0, 3, 3, 0]

Before: [0, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 3, 2, 3]
4 0 2 2
After:  [3, 3, 1, 3]

Before: [3, 2, 3, 3]
12 1 2 0
After:  [2, 2, 3, 3]

Before: [1, 1, 3, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [2, 3, 3, 3]
5 3 2 1
After:  [2, 1, 3, 3]

Before: [0, 1, 1, 2]
0 0 0 0
After:  [0, 1, 1, 2]

Before: [3, 1, 3, 2]
12 3 2 0
After:  [2, 1, 3, 2]

Before: [1, 3, 2, 1]
1 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 1, 3, 2]
14 1 3 1
After:  [0, 0, 3, 2]

Before: [1, 1, 2, 3]
7 1 3 1
After:  [1, 0, 2, 3]

Before: [2, 2, 3, 0]
12 0 2 1
After:  [2, 2, 3, 0]

Before: [0, 1, 2, 2]
14 1 3 1
After:  [0, 0, 2, 2]

Before: [1, 1, 1, 2]
13 3 3 2
After:  [1, 1, 0, 2]

Before: [3, 3, 2, 0]
4 0 2 0
After:  [1, 3, 2, 0]

Before: [2, 1, 2, 2]
11 2 2 0
After:  [2, 1, 2, 2]

Before: [0, 0, 1, 3]
0 0 0 2
After:  [0, 0, 0, 3]

Before: [1, 0, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [3, 2, 2, 2]
4 0 2 1
After:  [3, 1, 2, 2]

Before: [0, 2, 3, 3]
12 1 2 3
After:  [0, 2, 3, 2]

Before: [3, 3, 0, 3]
8 0 2 2
After:  [3, 3, 1, 3]

Before: [1, 1, 0, 2]
14 1 3 0
After:  [0, 1, 0, 2]

Before: [2, 3, 0, 3]
3 0 1 2
After:  [2, 3, 1, 3]

Before: [1, 1, 1, 1]
8 2 1 1
After:  [1, 0, 1, 1]

Before: [1, 1, 2, 0]
1 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 2, 2, 1]
5 2 1 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
1 0 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [0, 1, 1, 1]
9 1 3 1
After:  [0, 1, 1, 1]

Before: [1, 1, 0, 3]
6 1 0 0
After:  [1, 1, 0, 3]

Before: [1, 2, 2, 3]
1 0 2 0
After:  [0, 2, 2, 3]

Before: [3, 3, 1, 2]
13 3 3 2
After:  [3, 3, 0, 2]

Before: [2, 2, 2, 1]
15 3 2 3
After:  [2, 2, 2, 1]

Before: [1, 2, 1, 3]
7 1 3 1
After:  [1, 0, 1, 3]

Before: [1, 1, 0, 2]
9 0 2 3
After:  [1, 1, 0, 0]

Before: [3, 3, 0, 2]
8 0 2 1
After:  [3, 1, 0, 2]

Before: [1, 0, 0, 3]
11 3 3 3
After:  [1, 0, 0, 3]

Before: [0, 3, 2, 2]
0 0 0 2
After:  [0, 3, 0, 2]

Before: [2, 3, 3, 0]
3 0 1 0
After:  [1, 3, 3, 0]

Before: [3, 3, 2, 1]
3 2 0 2
After:  [3, 3, 1, 1]

Before: [1, 1, 2, 2]
14 1 3 3
After:  [1, 1, 2, 0]

Before: [3, 3, 1, 1]
13 2 3 3
After:  [3, 3, 1, 0]

Before: [3, 1, 2, 0]
4 0 2 3
After:  [3, 1, 2, 1]

Before: [0, 3, 2, 2]
3 2 1 3
After:  [0, 3, 2, 1]

Before: [3, 1, 2, 1]
15 3 2 2
After:  [3, 1, 1, 1]

Before: [3, 1, 2, 2]
2 1 2 2
After:  [3, 1, 0, 2]

Before: [0, 0, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [1, 1, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 3, 2, 2]
8 3 2 0
After:  [0, 3, 2, 2]

Before: [1, 2, 2, 1]
15 3 2 3
After:  [1, 2, 2, 1]

Before: [2, 0, 2, 1]
15 3 2 2
After:  [2, 0, 1, 1]

Before: [2, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 3, 2]
13 3 3 3
After:  [1, 3, 3, 0]

Before: [2, 0, 0, 2]
13 3 3 2
After:  [2, 0, 0, 2]

Before: [1, 0, 0, 0]
9 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 2, 3]
11 3 3 0
After:  [3, 2, 2, 3]

Before: [1, 3, 2, 1]
1 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 1, 3, 1]
9 1 3 1
After:  [3, 1, 3, 1]

Before: [0, 2, 3, 0]
12 1 2 2
After:  [0, 2, 2, 0]

Before: [1, 1, 3, 2]
6 1 0 0
After:  [1, 1, 3, 2]

Before: [3, 0, 2, 2]
8 3 2 1
After:  [3, 0, 2, 2]

Before: [1, 1, 0, 1]
9 0 2 0
After:  [0, 1, 0, 1]

Before: [1, 1, 2, 1]
9 1 3 1
After:  [1, 1, 2, 1]

Before: [2, 2, 2, 0]
5 2 0 0
After:  [1, 2, 2, 0]

Before: [3, 3, 2, 1]
15 3 2 2
After:  [3, 3, 1, 1]

Before: [0, 1, 1, 1]
9 1 3 3
After:  [0, 1, 1, 1]

Before: [1, 1, 3, 0]
6 1 0 1
After:  [1, 1, 3, 0]

Before: [0, 3, 1, 3]
0 0 0 2
After:  [0, 3, 0, 3]

Before: [2, 3, 3, 0]
8 2 0 1
After:  [2, 1, 3, 0]

Before: [3, 1, 3, 2]
14 1 3 1
After:  [3, 0, 3, 2]

Before: [0, 3, 1, 3]
7 2 3 0
After:  [0, 3, 1, 3]

Before: [2, 1, 3, 1]
4 0 1 2
After:  [2, 1, 1, 1]

Before: [0, 1, 3, 2]
0 0 0 2
After:  [0, 1, 0, 2]

Before: [2, 2, 3, 1]
12 0 2 2
After:  [2, 2, 2, 1]

Before: [3, 1, 3, 1]
13 3 3 3
After:  [3, 1, 3, 0]

Before: [3, 3, 2, 2]
3 2 1 0
After:  [1, 3, 2, 2]

Before: [0, 1, 2, 3]
2 1 2 2
After:  [0, 1, 0, 3]

Before: [3, 1, 2, 2]
3 2 0 0
After:  [1, 1, 2, 2]

Before: [0, 1, 1, 0]
8 2 1 3
After:  [0, 1, 1, 0]

Before: [1, 1, 2, 3]
1 0 2 0
After:  [0, 1, 2, 3]

Before: [1, 2, 0, 3]
7 1 3 3
After:  [1, 2, 0, 0]

Before: [2, 1, 3, 0]
10 1 3 1
After:  [2, 1, 3, 0]

Before: [3, 1, 2, 0]
3 2 0 0
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 1, 2, 0]
10 1 3 1
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 2]
5 2 0 1
After:  [2, 1, 2, 2]

Before: [2, 1, 0, 2]
14 1 3 0
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 1]
15 3 2 2
After:  [1, 1, 1, 1]

Before: [3, 1, 2, 0]
2 1 2 2
After:  [3, 1, 0, 0]

Before: [1, 1, 2, 3]
2 1 2 1
After:  [1, 0, 2, 3]

Before: [3, 0, 2, 2]
3 2 0 2
After:  [3, 0, 1, 2]

Before: [0, 0, 3, 2]
13 3 3 2
After:  [0, 0, 0, 2]

Before: [1, 0, 2, 2]
1 0 2 2
After:  [1, 0, 0, 2]

Before: [0, 1, 2, 3]
11 3 3 3
After:  [0, 1, 2, 3]

Before: [2, 0, 3, 3]
5 3 2 1
After:  [2, 1, 3, 3]

Before: [0, 2, 0, 3]
0 0 0 3
After:  [0, 2, 0, 0]

Before: [2, 2, 0, 1]
13 3 3 3
After:  [2, 2, 0, 0]

Before: [0, 1, 2, 2]
14 1 3 3
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 1]
4 0 1 1
After:  [2, 1, 2, 1]

Before: [1, 1, 3, 1]
9 1 3 0
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 3]
6 1 0 1
After:  [1, 1, 1, 3]

Before: [3, 1, 1, 0]
8 2 1 1
After:  [3, 0, 1, 0]

Before: [3, 2, 2, 1]
15 3 2 1
After:  [3, 1, 2, 1]

Before: [2, 1, 2, 3]
11 3 3 0
After:  [3, 1, 2, 3]

Before: [0, 0, 2, 1]
15 3 2 2
After:  [0, 0, 1, 1]

Before: [1, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [0, 3, 2, 2]
0 0 0 3
After:  [0, 3, 2, 0]

Before: [2, 1, 2, 0]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 2, 3]
3 2 1 0
After:  [1, 3, 2, 3]

Before: [1, 2, 2, 3]
1 0 2 3
After:  [1, 2, 2, 0]

Before: [2, 3, 0, 0]
3 0 1 3
After:  [2, 3, 0, 1]

Before: [2, 3, 1, 3]
3 0 1 1
After:  [2, 1, 1, 3]

Before: [3, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 1, 3, 2]
12 3 2 1
After:  [3, 2, 3, 2]

Before: [3, 1, 2, 3]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [2, 1, 2, 0]
2 1 2 2
After:  [2, 1, 0, 0]

Before: [0, 3, 2, 3]
0 0 0 3
After:  [0, 3, 2, 0]

Before: [1, 0, 0, 2]
13 3 3 3
After:  [1, 0, 0, 0]

Before: [2, 3, 3, 3]
3 0 1 1
After:  [2, 1, 3, 3]

Before: [0, 1, 0, 3]
7 1 3 3
After:  [0, 1, 0, 0]

Before: [0, 1, 2, 2]
2 1 2 2
After:  [0, 1, 0, 2]

Before: [2, 0, 3, 0]
8 2 0 3
After:  [2, 0, 3, 1]

Before: [2, 3, 2, 1]
15 3 2 3
After:  [2, 3, 2, 1]

Before: [0, 2, 3, 2]
13 3 3 3
After:  [0, 2, 3, 0]

Before: [0, 2, 2, 3]
7 1 3 2
After:  [0, 2, 0, 3]

Before: [3, 2, 1, 3]
7 1 3 3
After:  [3, 2, 1, 0]

Before: [2, 1, 1, 2]
14 1 3 0
After:  [0, 1, 1, 2]

Before: [3, 1, 2, 0]
4 0 2 2
After:  [3, 1, 1, 0]

Before: [1, 2, 3, 1]
12 1 2 0
After:  [2, 2, 3, 1]

Before: [0, 0, 3, 2]
12 3 2 3
After:  [0, 0, 3, 2]

Before: [2, 1, 2, 0]
10 1 3 3
After:  [2, 1, 2, 1]

Before: [2, 0, 3, 3]
12 0 2 3
After:  [2, 0, 3, 2]

Before: [1, 1, 1, 2]
14 1 3 2
After:  [1, 1, 0, 2]

Before: [0, 2, 0, 3]
11 3 3 2
After:  [0, 2, 3, 3]

Before: [3, 2, 1, 3]
7 2 3 3
After:  [3, 2, 1, 0]

Before: [3, 1, 2, 2]
8 3 2 3
After:  [3, 1, 2, 0]

Before: [2, 3, 2, 3]
3 0 1 0
After:  [1, 3, 2, 3]

Before: [2, 1, 2, 2]
4 0 1 3
After:  [2, 1, 2, 1]

Before: [3, 2, 2, 2]
3 2 0 2
After:  [3, 2, 1, 2]

Before: [3, 1, 2, 1]
4 0 2 2
After:  [3, 1, 1, 1]

Before: [2, 3, 2, 1]
15 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 3, 2]
4 0 1 3
After:  [2, 1, 3, 1]

Before: [0, 1, 3, 2]
14 1 3 0
After:  [0, 1, 3, 2]

Before: [1, 2, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 3, 0, 2]
9 0 2 0
After:  [0, 3, 0, 2]

Before: [1, 1, 3, 0]
6 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 0, 2, 0]
1 0 2 2
After:  [1, 0, 0, 0]

Before: [0, 1, 0, 3]
0 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 3, 2, 3]
1 0 2 1
After:  [1, 0, 2, 3]

Before: [3, 3, 2, 2]
3 2 1 2
After:  [3, 3, 1, 2]

Before: [2, 1, 0, 2]
4 0 1 3
After:  [2, 1, 0, 1]

Before: [2, 2, 1, 3]
7 2 3 0
After:  [0, 2, 1, 3]

Before: [2, 1, 2, 2]
4 0 1 2
After:  [2, 1, 1, 2]

Before: [2, 1, 3, 2]
12 3 2 3
After:  [2, 1, 3, 2]

Before: [2, 2, 3, 3]
5 3 2 1
After:  [2, 1, 3, 3]

Before: [0, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [0, 3, 2, 1]
13 3 3 3
After:  [0, 3, 2, 0]

Before: [0, 2, 3, 2]
12 3 2 1
After:  [0, 2, 3, 2]

Before: [0, 2, 3, 1]
0 0 0 0
After:  [0, 2, 3, 1]

Before: [1, 1, 0, 1]
9 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 2, 3, 3]
7 1 3 1
After:  [3, 0, 3, 3]

Before: [0, 3, 0, 3]
11 3 3 3
After:  [0, 3, 0, 3]

Before: [3, 3, 2, 1]
15 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 1]
6 1 0 1
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 3]
4 0 2 0
After:  [1, 3, 2, 3]

Before: [2, 3, 3, 0]
12 0 2 3
After:  [2, 3, 3, 2]

Before: [1, 3, 2, 0]
3 2 1 1
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 3]
3 2 0 1
After:  [3, 1, 2, 3]

Before: [0, 2, 3, 1]
12 1 2 0
After:  [2, 2, 3, 1]

Before: [3, 0, 2, 0]
3 2 0 1
After:  [3, 1, 2, 0]

Before: [1, 3, 2, 1]
1 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 1]
6 1 0 3
After:  [1, 1, 2, 1]

Before: [1, 2, 3, 2]
12 1 2 1
After:  [1, 2, 3, 2]

Before: [1, 1, 2, 1]
1 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 1, 0, 0]
10 1 3 0
After:  [1, 1, 0, 0]

Before: [1, 2, 2, 0]
5 2 1 1
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [0, 0, 0, 3]
0 0 0 0
After:  [0, 0, 0, 3]

Before: [1, 1, 1, 0]
6 1 0 0
After:  [1, 1, 1, 0]

Before: [1, 1, 2, 3]
1 0 2 2
After:  [1, 1, 0, 3]

Before: [3, 0, 2, 1]
4 0 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 0, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 0]
8 2 1 0
After:  [0, 1, 1, 0]

Before: [3, 2, 2, 3]
5 2 1 2
After:  [3, 2, 1, 3]

Before: [3, 3, 2, 1]
4 0 2 2
After:  [3, 3, 1, 1]

Before: [2, 3, 0, 2]
3 0 1 2
After:  [2, 3, 1, 2]

Before: [1, 3, 0, 2]
9 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 2, 0, 1]
9 0 2 1
After:  [1, 0, 0, 1]

Before: [2, 0, 2, 0]
5 2 0 3
After:  [2, 0, 2, 1]

Before: [1, 1, 3, 1]
8 3 1 2
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [2, 3, 3, 2]
8 2 0 2
After:  [2, 3, 1, 2]

Before: [3, 1, 0, 0]
10 1 3 1
After:  [3, 1, 0, 0]

Before: [1, 1, 0, 3]
9 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 2, 3, 2]
12 3 2 2
After:  [3, 2, 2, 2]

Before: [1, 3, 2, 0]
1 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 2, 0, 1]
13 3 3 0
After:  [0, 2, 0, 1]

Before: [0, 1, 3, 3]
5 3 2 3
After:  [0, 1, 3, 1]

Before: [1, 1, 1, 0]
10 1 3 1
After:  [1, 1, 1, 0]

Before: [2, 0, 2, 0]
5 2 0 1
After:  [2, 1, 2, 0]

Before: [0, 1, 2, 1]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 2, 3, 3]
7 1 3 0
After:  [0, 2, 3, 3]

Before: [0, 3, 0, 0]
0 0 0 0
After:  [0, 3, 0, 0]

Before: [3, 1, 3, 1]
8 3 1 1
After:  [3, 0, 3, 1]

Before: [0, 1, 3, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [2, 3, 1, 3]
3 0 1 0
After:  [1, 3, 1, 3]

Before: [1, 1, 0, 2]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 3, 2, 2]
3 2 1 1
After:  [1, 1, 2, 2]

Before: [0, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 1, 2, 0]
10 1 3 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 0]
11 2 2 0
After:  [2, 0, 2, 0]

Before: [0, 1, 0, 2]
13 3 3 0
After:  [0, 1, 0, 2]

Before: [1, 1, 0, 3]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 3, 2, 2]
1 0 2 3
After:  [1, 3, 2, 0]

Before: [3, 1, 2, 3]
2 1 2 2
After:  [3, 1, 0, 3]

Before: [3, 1, 2, 3]
4 0 2 0
After:  [1, 1, 2, 3]

Before: [2, 1, 3, 2]
12 0 2 3
After:  [2, 1, 3, 2]

Before: [3, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 0, 2]
8 0 2 0
After:  [1, 1, 0, 2]

Before: [2, 3, 2, 1]
15 3 2 2
After:  [2, 3, 1, 1]

Before: [3, 1, 0, 2]
13 3 3 3
After:  [3, 1, 0, 0]

Before: [3, 1, 2, 0]
10 1 3 3
After:  [3, 1, 2, 1]

Before: [0, 0, 1, 3]
0 0 0 1
After:  [0, 0, 1, 3]

Before: [3, 3, 3, 3]
11 3 3 2
After:  [3, 3, 3, 3]

Before: [0, 1, 1, 0]
10 1 3 3
After:  [0, 1, 1, 1]

Before: [3, 2, 2, 3]
5 2 1 3
After:  [3, 2, 2, 1]

Before: [1, 0, 0, 1]
9 0 2 2
After:  [1, 0, 0, 1]

Before: [2, 2, 2, 0]
5 2 1 0
After:  [1, 2, 2, 0]

Before: [1, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 1, 1, 2]
14 1 3 2
After:  [2, 1, 0, 2]

Before: [3, 2, 2, 3]
11 3 3 1
After:  [3, 3, 2, 3]

Before: [1, 1, 2, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [3, 0, 0, 1]
8 0 2 3
After:  [3, 0, 0, 1]

Before: [3, 3, 3, 3]
5 3 2 3
After:  [3, 3, 3, 1]

Before: [0, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 0, 1]
9 1 3 2
After:  [3, 1, 1, 1]

Before: [3, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [3, 2, 1, 3]
7 2 3 2
After:  [3, 2, 0, 3]

Before: [2, 1, 3, 3]
8 2 0 3
After:  [2, 1, 3, 1]

Before: [0, 3, 2, 3]
11 2 2 3
After:  [0, 3, 2, 2]

Before: [0, 1, 2, 1]
2 1 2 1
After:  [0, 0, 2, 1]

Before: [2, 1, 2, 1]
4 0 1 0
After:  [1, 1, 2, 1]

Before: [1, 1, 3, 0]
6 1 0 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 0]
4 0 1 1
After:  [2, 1, 2, 0]

Before: [0, 1, 0, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [1, 1, 1, 3]
7 1 3 3
After:  [1, 1, 1, 0]

Before: [0, 1, 1, 1]
0 0 0 0
After:  [0, 1, 1, 1]

Before: [1, 2, 3, 2]
12 3 2 2
After:  [1, 2, 2, 2]

Before: [1, 1, 0, 3]
7 1 3 3
After:  [1, 1, 0, 0]

Before: [1, 2, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [3, 1, 0, 2]
14 1 3 2
After:  [3, 1, 0, 2]

Before: [2, 3, 3, 3]
12 0 2 3
After:  [2, 3, 3, 2]

Before: [3, 2, 3, 1]
12 1 2 0
After:  [2, 2, 3, 1]

Before: [1, 1, 1, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 0, 2, 1]
11 2 2 3
After:  [0, 0, 2, 2]

Before: [0, 3, 1, 3]
0 0 0 1
After:  [0, 0, 1, 3]

Before: [2, 1, 3, 0]
8 2 0 2
After:  [2, 1, 1, 0]

Before: [2, 1, 3, 3]
12 0 2 1
After:  [2, 2, 3, 3]

Before: [1, 2, 3, 3]
12 1 2 1
After:  [1, 2, 3, 3]

Before: [1, 1, 0, 3]
6 1 0 2
After:  [1, 1, 1, 3]

Before: [3, 3, 2, 2]
4 0 2 3
After:  [3, 3, 2, 1]

Before: [3, 2, 0, 2]
13 3 3 3
After:  [3, 2, 0, 0]

Before: [1, 1, 0, 1]
6 1 0 1
After:  [1, 1, 0, 1]

Before: [3, 3, 2, 3]
7 2 3 0
After:  [0, 3, 2, 3]

Before: [3, 1, 2, 2]
2 1 2 1
After:  [3, 0, 2, 2]

Before: [3, 1, 3, 1]
9 1 3 2
After:  [3, 1, 1, 1]

Before: [3, 3, 2, 1]
15 3 2 3
After:  [3, 3, 2, 1]

Before: [0, 1, 3, 0]
10 1 3 1
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 2]
6 1 0 0
After:  [1, 1, 2, 2]

Before: [2, 0, 1, 1]
8 0 1 2
After:  [2, 0, 1, 1]

Before: [1, 1, 2, 3]
11 2 2 2
After:  [1, 1, 2, 3]

Before: [0, 3, 3, 2]
12 3 2 1
After:  [0, 2, 3, 2]

Before: [0, 1, 2, 1]
9 1 3 1
After:  [0, 1, 2, 1]

Before: [3, 0, 3, 3]
5 3 0 1
After:  [3, 1, 3, 3]

Before: [1, 0, 0, 1]
9 0 2 3
After:  [1, 0, 0, 0]

Before: [0, 1, 1, 0]
10 1 3 1
After:  [0, 1, 1, 0]

Before: [1, 1, 3, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 3, 3, 1]
5 2 3 0
After:  [0, 3, 3, 1]

Before: [3, 1, 2, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [3, 3, 2, 3]
11 3 3 0
After:  [3, 3, 2, 3]

Before: [1, 1, 0, 1]
8 3 1 2
After:  [1, 1, 0, 1]

Before: [0, 1, 3, 2]
14 1 3 3
After:  [0, 1, 3, 0]

Before: [2, 3, 0, 3]
3 0 1 3
After:  [2, 3, 0, 1]

Before: [2, 1, 3, 2]
12 0 2 2
After:  [2, 1, 2, 2]

Before: [2, 1, 0, 0]
10 1 3 3
After:  [2, 1, 0, 1]

Before: [3, 2, 2, 0]
3 2 0 0
After:  [1, 2, 2, 0]

Before: [2, 2, 2, 1]
13 3 3 2
After:  [2, 2, 0, 1]

Before: [3, 1, 3, 1]
5 2 3 1
After:  [3, 0, 3, 1]

Before: [2, 3, 3, 3]
12 0 2 1
After:  [2, 2, 3, 3]

Before: [1, 1, 1, 1]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 1, 0, 0]
10 1 3 0
After:  [1, 1, 0, 0]

Before: [3, 1, 2, 3]
7 1 3 0
After:  [0, 1, 2, 3]

Before: [2, 1, 2, 1]
15 3 2 2
After:  [2, 1, 1, 1]

Before: [3, 1, 3, 2]
13 3 3 2
After:  [3, 1, 0, 2]

Before: [0, 1, 3, 1]
8 3 1 2
After:  [0, 1, 0, 1]

Before: [0, 0, 3, 0]
0 0 0 0
After:  [0, 0, 3, 0]

Before: [2, 3, 3, 1]
12 0 2 1
After:  [2, 2, 3, 1]

Before: [0, 1, 3, 1]
9 1 3 0
After:  [1, 1, 3, 1]

Before: [3, 1, 1, 0]
10 1 3 3
After:  [3, 1, 1, 1]

Before: [1, 1, 0, 1]
6 1 0 0
After:  [1, 1, 0, 1]

Before: [0, 2, 0, 0]
0 0 0 0
After:  [0, 2, 0, 0]

Before: [3, 0, 2, 3]
3 2 0 0
After:  [1, 0, 2, 3]

Before: [0, 2, 2, 3]
0 0 0 2
After:  [0, 2, 0, 3]

Before: [0, 3, 3, 3]
11 3 3 2
After:  [0, 3, 3, 3]

Before: [3, 1, 1, 3]
5 3 0 3
After:  [3, 1, 1, 1]

Before: [1, 2, 0, 3]
11 3 3 2
After:  [1, 2, 3, 3]

Before: [0, 3, 1, 1]
0 0 0 1
After:  [0, 0, 1, 1]

Before: [2, 1, 0, 0]
10 1 3 1
After:  [2, 1, 0, 0]

Before: [2, 1, 0, 1]
9 1 3 1
After:  [2, 1, 0, 1]

Before: [2, 3, 2, 3]
3 2 1 1
After:  [2, 1, 2, 3]

Before: [0, 3, 0, 2]
0 0 0 3
After:  [0, 3, 0, 0]

Before: [0, 2, 2, 3]
11 2 2 2
After:  [0, 2, 2, 3]

Before: [3, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 3, 2, 3]
11 2 2 2
After:  [2, 3, 2, 3]

Before: [1, 0, 2, 1]
15 3 2 3
After:  [1, 0, 2, 1]

Before: [2, 3, 3, 2]
3 0 1 0
After:  [1, 3, 3, 2]

Before: [3, 3, 2, 2]
4 0 2 0
After:  [1, 3, 2, 2]

Before: [3, 1, 3, 2]
14 1 3 3
After:  [3, 1, 3, 0]

Before: [2, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 3]
5 3 0 0
After:  [1, 1, 3, 3]

Before: [0, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 1, 2, 3]
6 1 0 0
After:  [1, 1, 2, 3]

Before: [1, 3, 2, 2]
1 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 2, 0, 1]
9 0 2 0
After:  [0, 2, 0, 1]

Before: [3, 2, 2, 3]
4 0 2 0
After:  [1, 2, 2, 3]

Before: [2, 2, 3, 2]
12 0 2 2
After:  [2, 2, 2, 2]

Before: [2, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 1, 2, 3]
5 2 0 0
After:  [1, 1, 2, 3]

Before: [2, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 0]
3 2 1 0
After:  [1, 3, 2, 0]

Before: [1, 3, 2, 3]
1 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 0, 2, 1]
15 3 2 3
After:  [0, 0, 2, 1]

Before: [1, 3, 2, 2]
1 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 0, 3, 3]
5 3 0 0
After:  [1, 0, 3, 3]

Before: [2, 3, 1, 3]
7 2 3 2
After:  [2, 3, 0, 3]

Before: [0, 1, 0, 2]
14 1 3 1
After:  [0, 0, 0, 2]

Before: [2, 1, 2, 1]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 0, 1, 3]
7 2 3 1
After:  [2, 0, 1, 3]

Before: [1, 1, 1, 2]
14 1 3 0
After:  [0, 1, 1, 2]

Before: [2, 1, 0, 1]
4 0 1 0
After:  [1, 1, 0, 1]

Before: [2, 3, 0, 2]
3 0 1 0
After:  [1, 3, 0, 2]

Before: [2, 3, 2, 2]
5 2 0 3
After:  [2, 3, 2, 1]

Before: [0, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 3, 2]
14 1 3 2
After:  [1, 1, 0, 2]

Before: [1, 3, 0, 3]
9 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 3, 3, 1]
13 3 3 0
After:  [0, 3, 3, 1]

Before: [3, 2, 2, 1]
4 0 2 1
After:  [3, 1, 2, 1]

Before: [2, 3, 1, 1]
3 0 1 3
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 0]
9 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 1, 3, 0]
8 2 0 0
After:  [1, 1, 3, 0]

Before: [2, 2, 2, 0]
5 2 1 1
After:  [2, 1, 2, 0]

Before: [1, 1, 2, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 3, 1, 0]
0 0 0 2
After:  [0, 3, 0, 0]

Before: [1, 3, 2, 2]
8 3 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 1, 0]
10 1 3 2
After:  [1, 1, 1, 0]

Before: [1, 2, 2, 0]
11 2 2 1
After:  [1, 2, 2, 0]

Before: [2, 1, 2, 2]
11 2 2 2
After:  [2, 1, 2, 2]

Before: [1, 3, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [0, 2, 3, 3]
0 0 0 0
After:  [0, 2, 3, 3]

Before: [0, 2, 2, 3]
11 2 2 0
After:  [2, 2, 2, 3]

Before: [3, 2, 3, 3]
5 3 2 2
After:  [3, 2, 1, 3]

Before: [2, 0, 3, 3]
12 0 2 2
After:  [2, 0, 2, 3]

Before: [2, 1, 1, 1]
9 1 3 0
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 1]
9 1 3 2
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 2]
11 2 2 3
After:  [1, 1, 2, 2]

Before: [2, 1, 3, 2]
12 3 2 0
After:  [2, 1, 3, 2]

Before: [1, 1, 0, 2]
9 0 2 0
After:  [0, 1, 0, 2]

Before: [1, 1, 3, 3]
6 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 3, 0, 2]
13 3 3 2
After:  [1, 3, 0, 2]

Before: [1, 1, 0, 0]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [3, 2, 3, 3]
5 3 0 3
After:  [3, 2, 3, 1]

Before: [1, 1, 1, 3]
8 2 1 3
After:  [1, 1, 1, 0]

Before: [3, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 0, 2, 0]
1 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 1, 3, 3]
7 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 2]
14 1 3 1
After:  [2, 0, 0, 2]

Before: [0, 3, 2, 1]
15 3 2 3
After:  [0, 3, 2, 1]

Before: [2, 3, 3, 3]
3 0 1 3
After:  [2, 3, 3, 1]

Before: [3, 0, 2, 3]
4 0 2 1
After:  [3, 1, 2, 3]

Before: [0, 2, 1, 3]
7 2 3 1
After:  [0, 0, 1, 3]

Before: [1, 3, 2, 0]
3 2 1 3
After:  [1, 3, 2, 1]

Before: [3, 2, 3, 3]
5 3 0 0
After:  [1, 2, 3, 3]

Before: [2, 0, 0, 1]
8 0 1 0
After:  [1, 0, 0, 1]

Before: [2, 1, 3, 1]
9 1 3 2
After:  [2, 1, 1, 1]

Before: [0, 2, 2, 1]
11 2 2 1
After:  [0, 2, 2, 1]

Before: [0, 1, 0, 3]
0 0 0 3
After:  [0, 1, 0, 0]

Before: [2, 1, 1, 3]
4 0 1 1
After:  [2, 1, 1, 3]

Before: [3, 3, 2, 2]
3 2 0 0
After:  [1, 3, 2, 2]

Before: [2, 2, 3, 2]
12 1 2 0
After:  [2, 2, 3, 2]

Before: [3, 0, 2, 1]
11 2 2 2
After:  [3, 0, 2, 1]

Before: [2, 0, 3, 2]
8 2 0 0
After:  [1, 0, 3, 2]

Before: [0, 1, 2, 1]
0 0 0 0
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 1]
1 0 2 0
After:  [0, 2, 2, 1]

Before: [2, 1, 1, 1]
8 2 1 0
After:  [0, 1, 1, 1]

Before: [1, 1, 2, 2]
14 1 3 1
After:  [1, 0, 2, 2]

Before: [0, 3, 3, 2]
12 3 2 0
After:  [2, 3, 3, 2]

Before: [0, 3, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 2, 3, 0]
8 2 0 0
After:  [1, 2, 3, 0]

Before: [3, 3, 2, 1]
4 0 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 2]
14 1 3 2
After:  [1, 1, 0, 2]

Before: [3, 2, 3, 3]
12 1 2 1
After:  [3, 2, 3, 3]

Before: [1, 1, 2, 2]
6 1 0 1
After:  [1, 1, 2, 2]

Before: [2, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 3, 3, 3]
11 3 3 2
After:  [1, 3, 3, 3]

Before: [3, 3, 2, 2]
8 3 2 3
After:  [3, 3, 2, 0]

Before: [2, 1, 0, 1]
4 0 1 2
After:  [2, 1, 1, 1]

Before: [1, 1, 0, 3]
7 1 3 2
After:  [1, 1, 0, 3]

Before: [2, 3, 3, 2]
12 3 2 3
After:  [2, 3, 3, 2]

Before: [1, 2, 0, 3]
9 0 2 0
After:  [0, 2, 0, 3]

Before: [1, 0, 0, 0]
9 0 2 0
After:  [0, 0, 0, 0]

Before: [2, 2, 3, 3]
12 0 2 0
After:  [2, 2, 3, 3]

Before: [2, 3, 3, 3]
11 3 3 1
After:  [2, 3, 3, 3]

Before: [0, 3, 2, 3]
11 2 2 1
After:  [0, 2, 2, 3]

Before: [2, 2, 3, 3]
12 1 2 0
After:  [2, 2, 3, 3]

Before: [3, 1, 1, 0]
10 1 3 1
After:  [3, 1, 1, 0]

Before: [3, 1, 2, 1]
9 1 3 3
After:  [3, 1, 2, 1]

Before: [1, 2, 1, 3]
7 1 3 3
After:  [1, 2, 1, 0]

Before: [2, 1, 2, 1]
2 1 2 2
After:  [2, 1, 0, 1]

Before: [2, 1, 3, 2]
14 1 3 1
After:  [2, 0, 3, 2]

Before: [1, 1, 1, 3]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 1, 1, 2]
14 1 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 0, 3]
8 0 2 0
After:  [1, 1, 0, 3]

Before: [1, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 2]
13 3 3 1
After:  [0, 0, 2, 2]

Before: [3, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 1, 2]
6 1 0 0
After:  [1, 1, 1, 2]

Before: [1, 1, 2, 1]
13 3 3 2
After:  [1, 1, 0, 1]

Before: [0, 1, 1, 1]
0 0 0 3
After:  [0, 1, 1, 0]

Before: [0, 1, 0, 0]
10 1 3 3
After:  [0, 1, 0, 1]

Before: [1, 1, 0, 0]
6 1 0 1
After:  [1, 1, 0, 0]

Before: [0, 1, 2, 1]
13 3 3 0
After:  [0, 1, 2, 1]

Before: [1, 3, 2, 3]
3 2 1 0
After:  [1, 3, 2, 3]

Before: [1, 2, 0, 2]
9 0 2 2
After:  [1, 2, 0, 2]

Before: [1, 3, 2, 1]
15 3 2 3
After:  [1, 3, 2, 1]

Before: [2, 2, 0, 3]
7 1 3 2
After:  [2, 2, 0, 3]

Before: [1, 1, 2, 3]
7 1 3 0
After:  [0, 1, 2, 3]

Before: [1, 0, 2, 1]
1 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 2, 2, 2]
1 0 2 0
After:  [0, 2, 2, 2]

Before: [1, 1, 0, 3]
6 1 0 1
After:  [1, 1, 0, 3]

Before: [1, 2, 2, 2]
1 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 3]
7 2 3 2
After:  [1, 1, 0, 3]

Before: [1, 1, 0, 2]
14 1 3 3
After:  [1, 1, 0, 0]

Before: [0, 1, 1, 2]
0 0 0 3
After:  [0, 1, 1, 0]

Before: [1, 0, 1, 1]
13 2 3 3
After:  [1, 0, 1, 0]

Before: [3, 1, 2, 2]
14 1 3 1
After:  [3, 0, 2, 2]

Before: [2, 1, 1, 0]
4 0 1 2
After:  [2, 1, 1, 0]

Before: [0, 2, 1, 1]
13 3 3 0
After:  [0, 2, 1, 1]

Before: [0, 3, 1, 3]
11 3 3 1
After:  [0, 3, 1, 3]

Before: [1, 3, 0, 2]
9 0 2 3
After:  [1, 3, 0, 0]

Before: [3, 2, 2, 3]
7 2 3 0
After:  [0, 2, 2, 3]

Before: [2, 1, 2, 2]
2 1 2 1
After:  [2, 0, 2, 2]

Before: [2, 2, 2, 1]
15 3 2 2
After:  [2, 2, 1, 1]

Before: [3, 3, 1, 1]
13 3 3 3
After:  [3, 3, 1, 0]

Before: [2, 2, 2, 3]
5 2 0 3
After:  [2, 2, 2, 1]

Before: [0, 3, 2, 3]
11 3 3 3
After:  [0, 3, 2, 3]

Before: [2, 3, 2, 0]
3 2 1 2
After:  [2, 3, 1, 0]

Before: [2, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 3, 1, 3]
7 2 3 2
After:  [3, 3, 0, 3]

Before: [3, 0, 2, 0]
11 2 2 0
After:  [2, 0, 2, 0]

Before: [0, 3, 1, 2]
0 0 0 2
After:  [0, 3, 0, 2]

Before: [1, 1, 2, 0]
2 1 2 1
After:  [1, 0, 2, 0]

Before: [3, 1, 3, 2]
12 3 2 3
After:  [3, 1, 3, 2]

Before: [0, 0, 1, 2]
0 0 0 0
After:  [0, 0, 1, 2]

Before: [3, 1, 1, 1]
8 3 1 1
After:  [3, 0, 1, 1]

Before: [0, 0, 2, 1]
0 0 0 0
After:  [0, 0, 2, 1]

Before: [1, 1, 2, 3]
1 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 3, 2, 0]
3 2 1 1
After:  [2, 1, 2, 0]

Before: [1, 3, 3, 2]
12 3 2 1
After:  [1, 2, 3, 2]

Before: [0, 1, 3, 2]
0 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 1, 2, 0]
10 1 3 2
After:  [2, 1, 1, 0]

Before: [2, 2, 3, 2]
12 0 2 0
After:  [2, 2, 3, 2]

Before: [2, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [3, 1, 3, 3]
11 3 3 2
After:  [3, 1, 3, 3]

Before: [3, 1, 3, 0]
10 1 3 3
After:  [3, 1, 3, 1]

Before: [0, 1, 1, 3]
7 2 3 0
After:  [0, 1, 1, 3]

Before: [1, 1, 2, 0]
1 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 1, 0]
10 1 3 3
After:  [1, 1, 1, 1]

Before: [1, 1, 3, 2]
13 3 3 3
After:  [1, 1, 3, 0]

Before: [2, 0, 3, 1]
8 0 1 0
After:  [1, 0, 3, 1]

Before: [3, 2, 2, 3]
3 2 0 0
After:  [1, 2, 2, 3]

Before: [0, 3, 2, 3]
0 0 0 2
After:  [0, 3, 0, 3]

Before: [2, 2, 1, 2]
13 3 3 3
After:  [2, 2, 1, 0]

Before: [0, 2, 3, 3]
5 3 2 0
After:  [1, 2, 3, 3]

Before: [2, 1, 2, 2]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 1, 0, 3]
4 0 1 1
After:  [2, 1, 0, 3]

Before: [2, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [2, 3, 3, 2]
12 3 2 1
After:  [2, 2, 3, 2]

Before: [3, 2, 3, 1]
5 2 3 2
After:  [3, 2, 0, 1]

Before: [3, 3, 3, 1]
5 2 3 1
After:  [3, 0, 3, 1]

Before: [1, 1, 3, 3]
7 1 3 1
After:  [1, 0, 3, 3]

Before: [2, 1, 2, 3]
2 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 1]
5 2 3 0
After:  [0, 1, 3, 1]

Before: [0, 2, 3, 3]
12 1 2 2
After:  [0, 2, 2, 3]

Before: [1, 0, 2, 2]
1 0 2 0
After:  [0, 0, 2, 2]

Before: [1, 1, 1, 2]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 3, 3, 1]
13 3 3 0
After:  [0, 3, 3, 1]

Before: [2, 1, 2, 1]
4 0 1 3
After:  [2, 1, 2, 1]

Before: [1, 1, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [0, 3, 1, 2]
0 0 0 0
After:  [0, 3, 1, 2]

Before: [3, 3, 2, 2]
4 0 2 1
After:  [3, 1, 2, 2]

Before: [0, 3, 2, 2]
3 2 1 2
After:  [0, 3, 1, 2]

Before: [3, 1, 1, 3]
7 2 3 3
After:  [3, 1, 1, 0]

Before: [2, 1, 2, 1]
15 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 1, 0]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 3, 3, 2]
12 3 2 2
After:  [1, 3, 2, 2]

Before: [3, 1, 1, 2]
14 1 3 1
After:  [3, 0, 1, 2]

Before: [0, 2, 2, 3]
0 0 0 0
After:  [0, 2, 2, 3]

Before: [1, 1, 2, 3]
6 1 0 3
After:  [1, 1, 2, 1]

Before: [1, 1, 1, 0]
6 1 0 1
After:  [1, 1, 1, 0]

Before: [2, 3, 1, 3]
7 2 3 3
After:  [2, 3, 1, 0]

Before: [0, 1, 3, 0]
0 0 0 0
After:  [0, 1, 3, 0]

Before: [3, 0, 0, 3]
11 3 3 0
After:  [3, 0, 0, 3]

Before: [3, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [3, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 1, 1]
6 1 0 1
After:  [1, 1, 1, 1]



1 2 3 0
1 0 0 3
0 2 0 2
6 2 3 2
8 3 2 0
0 0 3 0
10 1 0 1
15 1 1 2
1 3 3 3
1 1 3 0
1 2 0 1
1 1 3 0
0 0 2 0
10 0 2 2
15 2 0 3
1 0 2 1
1 1 1 0
1 3 0 2
0 0 2 0
0 0 2 0
10 0 3 3
15 3 3 1
1 0 0 2
1 3 0 0
1 0 1 3
13 2 0 0
0 0 1 0
10 1 0 1
15 1 2 0
1 2 2 2
1 1 3 1
12 2 3 3
0 3 1 3
0 3 1 3
10 0 3 0
15 0 1 1
1 3 1 2
1 0 1 3
1 3 2 0
2 0 2 2
0 2 1 2
10 1 2 1
15 1 1 2
0 2 0 0
6 0 1 0
0 0 0 1
6 1 2 1
1 2 1 3
12 1 3 0
0 0 3 0
10 0 2 2
15 2 1 0
1 3 3 1
1 0 2 3
1 3 1 2
8 3 2 3
0 3 3 3
10 0 3 0
15 0 2 3
1 3 1 0
1 0 2 2
1 0 2 1
13 2 0 0
0 0 3 0
10 0 3 3
1 3 2 2
0 0 0 0
6 0 3 0
1 2 1 1
11 1 0 0
0 0 3 0
10 3 0 3
1 1 3 0
0 3 0 1
6 1 1 1
1 2 2 2
15 0 2 1
0 1 2 1
10 3 1 3
15 3 0 2
1 3 2 1
1 2 2 3
1 0 2 0
14 1 3 1
0 1 3 1
0 1 2 1
10 2 1 2
15 2 3 0
1 3 2 2
1 3 1 1
2 1 2 3
0 3 3 3
10 0 3 0
15 0 3 1
0 3 0 3
6 3 1 3
1 1 3 0
1 2 0 2
15 0 2 0
0 0 1 0
10 0 1 1
15 1 1 0
1 3 2 1
1 0 3 2
1 2 3 2
0 2 1 2
10 2 0 0
15 0 2 1
1 1 3 0
1 0 3 3
1 2 3 2
7 3 2 3
0 3 3 3
10 3 1 1
15 1 2 0
0 2 0 2
6 2 0 2
1 3 0 3
1 0 0 1
2 3 2 3
0 3 1 3
10 3 0 0
15 0 2 3
1 3 1 0
0 3 0 1
6 1 3 1
2 0 2 2
0 2 3 2
10 2 3 3
15 3 0 2
1 2 2 0
1 2 0 3
0 1 0 1
6 1 2 1
5 0 3 0
0 0 2 0
10 2 0 2
15 2 3 0
1 0 1 2
0 1 0 1
6 1 1 1
1 1 2 3
0 3 2 2
0 2 3 2
0 2 2 2
10 2 0 0
15 0 1 2
1 1 2 0
1 0 1 3
1 3 0 1
6 0 1 0
0 0 1 0
0 0 3 0
10 2 0 2
15 2 0 1
0 1 0 0
6 0 0 0
1 2 2 2
7 3 2 3
0 3 2 3
0 3 2 3
10 3 1 1
1 0 2 3
12 2 3 0
0 0 2 0
10 1 0 1
0 2 0 3
6 3 3 3
0 0 0 2
6 2 0 2
0 3 0 0
6 0 2 0
2 3 2 3
0 3 1 3
10 3 1 1
1 2 3 3
1 3 3 2
1 1 3 0
9 0 3 2
0 2 1 2
10 2 1 1
15 1 1 3
1 3 3 2
1 0 0 1
6 0 1 1
0 1 3 1
10 1 3 3
15 3 2 2
1 3 2 3
1 1 0 1
10 0 0 1
0 1 1 1
10 2 1 2
15 2 1 1
1 0 2 2
1 3 1 0
0 0 0 3
6 3 2 3
8 2 3 3
0 3 2 3
10 3 1 1
15 1 0 2
1 2 0 0
1 1 1 3
0 2 0 1
6 1 3 1
4 0 3 1
0 1 2 1
0 1 2 1
10 2 1 2
1 3 1 1
1 2 3 3
3 0 1 0
0 0 2 0
10 2 0 2
15 2 3 1
1 0 3 2
1 3 3 0
8 2 3 0
0 0 2 0
0 0 2 0
10 0 1 1
15 1 3 0
1 2 2 2
1 3 2 1
1 0 2 3
7 3 2 1
0 1 2 1
10 0 1 0
15 0 0 3
0 0 0 2
6 2 0 2
1 3 1 1
1 1 1 0
6 0 1 0
0 0 3 0
0 0 2 0
10 3 0 3
15 3 3 1
1 1 2 0
0 2 0 2
6 2 2 2
1 0 1 3
7 3 2 2
0 2 1 2
10 2 1 1
15 1 1 2
0 1 0 0
6 0 2 0
1 2 2 1
1 1 1 3
4 0 3 1
0 1 2 1
10 1 2 2
0 1 0 3
6 3 2 3
0 1 0 1
6 1 1 1
1 1 1 0
10 1 0 1
0 1 2 1
10 1 2 2
15 2 3 3
0 3 0 1
6 1 3 1
0 1 0 2
6 2 0 2
6 0 1 1
0 1 3 1
10 3 1 3
15 3 1 0
1 2 0 3
0 2 0 1
6 1 3 1
8 2 3 3
0 3 3 3
10 0 3 0
1 1 1 3
1 0 0 1
0 3 2 3
0 3 1 3
10 3 0 0
15 0 3 1
1 1 3 3
1 3 1 0
0 2 0 2
6 2 2 2
11 2 0 0
0 0 1 0
10 1 0 1
15 1 3 0
1 0 0 3
0 2 0 2
6 2 3 2
1 1 3 1
0 1 2 3
0 3 1 3
0 3 3 3
10 0 3 0
15 0 1 2
1 1 3 0
0 2 0 1
6 1 0 1
1 1 0 3
6 0 1 1
0 1 3 1
10 2 1 2
15 2 3 0
1 3 2 1
1 0 2 2
6 3 1 2
0 2 3 2
10 2 0 0
1 0 3 1
1 0 3 3
0 3 0 2
6 2 2 2
7 3 2 1
0 1 3 1
10 0 1 0
15 0 2 1
1 1 3 3
0 3 0 0
6 0 3 0
0 2 0 2
6 2 0 2
1 2 3 3
0 3 1 3
10 1 3 1
15 1 1 2
1 2 3 3
1 2 3 1
14 0 1 0
0 0 1 0
10 2 0 2
15 2 0 0
0 0 0 3
6 3 0 3
1 2 0 2
1 0 2 1
7 3 2 2
0 2 1 2
0 2 3 2
10 0 2 0
15 0 3 3
1 2 2 2
1 2 2 1
0 1 0 0
6 0 3 0
11 1 0 1
0 1 3 1
10 1 3 3
15 3 3 1
1 2 1 0
0 0 0 3
6 3 1 3
1 0 0 2
4 0 3 3
0 3 1 3
10 3 1 1
15 1 1 3
1 1 3 0
1 1 1 1
10 1 0 2
0 2 3 2
10 2 3 3
15 3 1 1
1 2 1 3
1 2 2 2
12 2 3 3
0 3 3 3
10 1 3 1
15 1 3 2
1 2 1 1
1 2 2 3
1 3 2 0
14 0 3 1
0 1 1 1
10 1 2 2
1 2 0 1
11 1 0 1
0 1 3 1
0 1 2 1
10 1 2 2
1 2 2 1
14 0 1 1
0 1 2 1
0 1 2 1
10 1 2 2
15 2 0 0
1 0 2 2
1 3 3 1
0 0 0 3
6 3 3 3
2 3 2 1
0 1 1 1
10 0 1 0
15 0 1 1
1 0 2 3
0 1 0 2
6 2 3 2
1 1 3 0
8 3 2 3
0 3 2 3
0 3 3 3
10 3 1 1
15 1 3 2
1 2 3 3
1 2 3 1
0 0 0 0
6 0 2 0
5 0 3 3
0 3 1 3
10 2 3 2
15 2 0 3
1 1 0 0
0 3 0 2
6 2 0 2
0 0 2 0
0 0 2 0
10 0 3 3
15 3 3 1
0 1 0 0
6 0 3 0
1 2 1 3
1 1 3 2
2 0 2 3
0 3 1 3
0 3 2 3
10 1 3 1
1 1 1 0
1 2 3 3
1 2 3 2
15 0 2 3
0 3 1 3
10 1 3 1
1 3 3 0
1 1 2 3
3 2 0 3
0 3 1 3
0 3 2 3
10 1 3 1
15 1 2 0
1 3 2 2
1 1 0 3
1 3 3 1
2 1 2 3
0 3 3 3
0 3 3 3
10 3 0 0
1 0 0 3
0 1 0 1
6 1 2 1
1 2 3 2
7 3 2 1
0 1 2 1
10 0 1 0
15 0 3 2
1 2 0 0
1 2 0 3
1 3 2 1
5 0 3 1
0 1 3 1
0 1 1 1
10 1 2 2
15 2 3 1
1 3 0 3
1 1 2 0
0 1 0 2
6 2 0 2
2 3 2 3
0 3 3 3
10 1 3 1
15 1 1 2
1 3 0 1
1 2 1 3
1 0 2 0
14 1 3 3
0 3 3 3
0 3 3 3
10 3 2 2
15 2 1 1
1 0 2 2
1 2 3 0
0 0 0 3
6 3 1 3
0 3 2 0
0 0 3 0
10 1 0 1
15 1 0 3
1 2 2 2
1 1 3 0
1 3 0 1
10 0 0 0
0 0 3 0
10 3 0 3
15 3 0 0
0 3 0 2
6 2 0 2
1 1 1 3
6 3 1 3
0 3 1 3
0 3 3 3
10 0 3 0
15 0 1 1
0 0 0 2
6 2 2 2
1 1 2 3
1 2 0 0
4 0 3 3
0 3 1 3
0 3 2 3
10 1 3 1
1 0 1 0
1 0 0 2
1 2 3 3
8 2 3 3
0 3 2 3
10 1 3 1
1 3 3 0
1 2 1 3
14 0 3 2
0 2 3 2
10 1 2 1
15 1 0 2
1 2 0 0
1 3 1 1
3 0 1 3
0 3 3 3
10 2 3 2
15 2 2 3
1 3 0 2
14 1 0 2
0 2 3 2
10 3 2 3
15 3 3 1
1 0 2 0
1 0 2 2
0 1 0 3
6 3 2 3
1 2 0 0
0 0 1 0
0 0 1 0
10 1 0 1
15 1 3 3
1 3 3 1
1 2 3 0
1 1 1 2
14 1 0 1
0 1 3 1
10 1 3 3
15 3 0 2
1 0 2 1
1 2 1 3
5 0 3 1
0 1 1 1
10 2 1 2
15 2 3 1
1 0 1 3
1 1 0 0
1 2 1 2
7 3 2 0
0 0 3 0
0 0 2 0
10 1 0 1
0 2 0 0
6 0 3 0
1 1 2 3
1 3 3 2
0 3 2 0
0 0 2 0
10 0 1 1
15 1 0 0
1 0 3 2
0 1 0 1
6 1 0 1
6 3 1 1
0 1 1 1
10 1 0 0
15 0 1 3
1 1 0 0
1 0 2 1
6 0 1 1
0 1 2 1
0 1 3 1
10 3 1 3
15 3 1 0
1 0 1 1
1 2 3 3
8 2 3 3
0 3 1 3
0 3 1 3
10 3 0 0
15 0 0 1
1 1 1 3
0 0 0 0
6 0 2 0
1 2 0 2
9 3 0 3
0 3 3 3
0 3 1 3
10 1 3 1
1 3 3 2
1 2 2 3
13 0 2 2
0 2 1 2
10 2 1 1
15 1 0 0
1 0 0 3
1 1 3 1
1 2 2 2
7 3 2 3
0 3 2 3
0 3 3 3
10 3 0 0
15 0 2 1
1 1 2 0
1 3 2 2
1 2 0 3
9 0 3 3
0 3 3 3
10 3 1 1
1 1 0 3
1 2 2 0
9 3 0 2
0 2 3 2
10 1 2 1
1 0 0 2
9 3 0 0
0 0 3 0
10 1 0 1
15 1 3 2
1 2 0 1
1 2 2 0
9 3 0 0
0 0 2 0
10 2 0 2
1 2 2 3
1 2 1 0
12 1 3 3
0 3 1 3
10 3 2 2
1 1 0 0
0 1 0 3
6 3 2 3
9 0 3 1
0 1 1 1
10 1 2 2
15 2 2 0
0 2 0 2
6 2 3 2
1 3 0 1
14 1 3 2
0 2 2 2
10 0 2 0
15 0 1 2
1 2 1 0
0 1 0 1
6 1 1 1
1 1 0 3
4 0 3 3
0 3 2 3
10 2 3 2
15 2 0 0
0 3 0 3
6 3 0 3
1 2 3 2
7 3 2 1
0 1 3 1
10 1 0 0
15 0 2 1
1 2 0 0
0 2 0 3
6 3 3 3
1 3 2 2
13 0 2 0
0 0 2 0
0 0 1 0
10 1 0 1
1 2 3 2
1 0 3 3
1 0 1 0
12 2 3 2
0 2 2 2
10 1 2 1
15 1 1 2
1 0 0 1
1 2 1 3
1 2 3 0
5 0 3 3
0 3 2 3
10 3 2 2
15 2 1 3
1 3 1 0
1 2 3 2
3 2 0 1
0 1 2 1
10 1 3 3
15 3 1 1
0 1 0 0
6 0 2 0
0 3 0 3
6 3 1 3
4 0 3 2
0 2 1 2
10 2 1 1
15 1 0 3
1 1 0 0
1 0 0 1
1 1 2 2
6 0 1 1
0 1 3 1
10 1 3 3
15 3 0 0
0 1 0 1
6 1 2 1
1 3 1 3
1 0 0 2
14 3 1 2
0 2 1 2
10 0 2 0
15 0 3 3
0 3 0 2
6 2 1 2
1 3 0 0
0 1 0 1
6 1 3 1
2 0 2 1
0 1 2 1
10 1 3 3
15 3 3 1
1 2 0 0
1 2 2 2
1 1 2 3
4 0 3 0
0 0 2 0
10 0 1 1
15 1 1 3
1 3 0 1
1 1 2 0
1 0 2 2
0 0 2 1
0 1 2 1
10 3 1 3
1 2 0 1
1 2 3 2
15 0 2 0
0 0 1 0
10 0 3 3
15 3 1 0
1 3 1 1
0 1 0 3
6 3 1 3
6 3 1 3
0 3 3 3
10 0 3 0
15 0 3 1
1 0 0 3
1 3 0 0
11 2 0 2
0 2 1 2
10 1 2 1
1 0 1 2
1 0 0 0
1 3 0 2
0 2 3 2
10 2 1 1
1 1 2 0
1 0 3 2
1 1 3 3
0 3 2 3
0 3 2 3
10 1 3 1
15 1 0 3
1 2 3 2
1 3 0 0
1 3 0 1
3 2 1 0
0 0 3 0
10 0 3 3
15 3 1 2
1 2 1 1
1 0 1 3
0 1 0 0
6 0 3 0
14 0 1 3
0 3 1 3
0 3 2 3
10 2 3 2
15 2 0 1
0 2 0 3
6 3 0 3
1 3 0 2
1 2 1 0
12 0 3 3
0 3 3 3
10 3 1 1
15 1 3 0
0 3 0 3
6 3 0 3
1 1 3 1
0 1 2 2
0 2 1 2
10 0 2 0
15 0 2 2
1 2 0 3
1 2 2 0
5 0 3 1
0 1 3 1
10 1 2 2
15 2 2 1
1 3 2 2
1 3 1 3
2 3 2 0
0 0 1 0
0 0 1 0
10 0 1 1
0 1 0 2
6 2 2 2
1 2 0 3
1 2 0 0
12 2 3 2
0 2 2 2
0 2 1 2
10 2 1 1
15 1 3 3
1 1 1 0
1 3 2 2
1 2 1 1
11 1 2 0
0 0 3 0
10 0 3 3
15 3 2 1
1 2 2 0
1 3 2 3
2 3 2 2
0 2 3 2
0 2 2 2
10 2 1 1
1 0 1 2
1 1 2 3
4 0 3 2
0 2 2 2
10 2 1 1
15 1 3 0
0 2 0 2
6 2 2 2
1 0 2 3
1 0 0 1
7 3 2 3
0 3 1 3
10 3 0 0
1 2 1 3
1 2 3 1
1 1 0 2
12 1 3 2
0 2 1 2
0 2 2 2
10 0 2 0
1 0 0 2
8 2 3 1
0 1 2 1
10 1 0 0
15 0 1 3
1 2 3 2
0 0 0 0
6 0 1 0
1 3 0 1
15 0 2 1
0 1 2 1
10 3 1 3
15 3 2 1
1 2 1 0
1 1 0 2
0 2 0 3
6 3 2 3
5 0 3 2
0 2 2 2
10 2 1 1
15 1 1 0
1 1 2 3
0 0 0 1
6 1 0 1
0 1 0 2
6 2 1 2
10 3 3 2
0 2 1 2
10 0 2 0
15 0 2 2
1 2 3 0
1 2 1 1
1 2 0 3
12 1 3 0
0 0 2 0
10 2 0 2
0 1 0 1
6 1 3 1
1 1 1 3
1 0 0 0
6 3 1 3
0 3 2 3
10 2 3 2
15 2 1 0
1 3 1 2
1 0 1 3
8 3 2 2
0 2 2 2
10 0 2 0
15 0 1 2
1 1 2 1
1 1 0 0
1 1 0 3
10 0 0 0
0 0 2 0
0 0 3 0
10 0 2 2
15 2 0 0
0 0 0 2
6 2 2 2
0 3 0 1
6 1 2 1
10 3 3 3
0 3 1 3
0 3 1 3
10 3 0 0
15 0 0 1
1 3 0 0
1 3 2 3
3 2 0 2
0 2 3 2
10 2 1 1
15 1 1 3
1 1 3 1
1 3 1 2
0 1 2 1
0 1 2 1
10 3 1 3
15 3 2 0
'''
)