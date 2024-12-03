from collections import defaultdict
def p1(a):
	a = a.strip().split("\n")
	g = defaultdict(set)
	r = defaultdict(set)
	for rec in a:
		x = rec.split(" ")
		u, v = x[1], x[7]
		g[u].add(v)
		r[v].add(u)
	every = g.keys() | r.keys()
	f = [x for x in every if x not in r]
	o = []
	while len(f):
		f.sort()
		h, f = f[0], f[1:]
		o.append(h)
		for y in g[h]:
			r[y].remove(h)
			if len(r[y]) == 0:
				f.append(y)
	print("Part 1:", "".join(o))
def p2(a):
	a = a.strip().split("\n")
	g = defaultdict(set)
	r = defaultdict(set)
	for rec in a:
		x = rec.split(" ")
		u, v = x[1], x[7]
		g[u].add(v)
		r[v].add(u)
	every = g.keys() | r.keys()
	f = [x for x in every if x not in r]
	W = [0] * 5
	for t in range(10**20):
		f.sort()
		for i in range(len(W)):
			if W[i] == 0:
			else:
				W[i] -= 1
				if W[i] == 0:
					
	while len(f):
		f.sort()
		h, f = f[0], f[1:]
		o.append(h)
		for y in g[h]:
			r[y].remove(h)
			if len(r[y]) == 0:
				f.append(y)
	print("Part 1:", "".join(o))
def solve(a):
	p1(a)
	p2(a)
solve(
'''
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''
)

solve(
'''
Step G must be finished before step M can begin.
Step T must be finished before step E can begin.
Step P must be finished before step M can begin.
Step V must be finished before step L can begin.
Step Y must be finished before step B can begin.
Step K must be finished before step Z can begin.
Step H must be finished before step I can begin.
Step D must be finished before step U can begin.
Step C must be finished before step L can begin.
Step R must be finished before step Z can begin.
Step U must be finished before step B can begin.
Step J must be finished before step M can begin.
Step M must be finished before step E can begin.
Step I must be finished before step X can begin.
Step N must be finished before step O can begin.
Step S must be finished before step F can begin.
Step X must be finished before step A can begin.
Step F must be finished before step Q can begin.
Step B must be finished before step Z can begin.
Step Q must be finished before step W can begin.
Step L must be finished before step W can begin.
Step O must be finished before step Z can begin.
Step A must be finished before step Z can begin.
Step E must be finished before step W can begin.
Step W must be finished before step Z can begin.
Step G must be finished before step R can begin.
Step H must be finished before step A can begin.
Step A must be finished before step W can begin.
Step Y must be finished before step D can begin.
Step O must be finished before step A can begin.
Step V must be finished before step U can begin.
Step H must be finished before step W can begin.
Step K must be finished before step F can begin.
Step J must be finished before step X can begin.
Step V must be finished before step R can begin.
Step Q must be finished before step A can begin.
Step F must be finished before step B can begin.
Step G must be finished before step P can begin.
Step L must be finished before step A can begin.
Step B must be finished before step Q can begin.
Step H must be finished before step J can begin.
Step J must be finished before step L can begin.
Step F must be finished before step E can begin.
Step U must be finished before step A can begin.
Step G must be finished before step Q can begin.
Step G must be finished before step S can begin.
Step K must be finished before step J can begin.
Step N must be finished before step B can begin.
Step F must be finished before step O can begin.
Step C must be finished before step Z can begin.
Step B must be finished before step E can begin.
Step M must be finished before step S can begin.
Step A must be finished before step E can begin.
Step E must be finished before step Z can begin.
Step K must be finished before step I can begin.
Step P must be finished before step A can begin.
Step Y must be finished before step L can begin.
Step Y must be finished before step J can begin.
Step G must be finished before step N can begin.
Step Q must be finished before step L can begin.
Step D must be finished before step X can begin.
Step C must be finished before step I can begin.
Step K must be finished before step B can begin.
Step N must be finished before step F can begin.
Step D must be finished before step M can begin.
Step B must be finished before step A can begin.
Step U must be finished before step J can begin.
Step Q must be finished before step Z can begin.
Step X must be finished before step F can begin.
Step K must be finished before step X can begin.
Step U must be finished before step E can begin.
Step X must be finished before step W can begin.
Step K must be finished before step Q can begin.
Step I must be finished before step E can begin.
Step D must be finished before step J can begin.
Step P must be finished before step I can begin.
Step K must be finished before step D can begin.
Step S must be finished before step X can begin.
Step C must be finished before step R can begin.
Step P must be finished before step W can begin.
Step I must be finished before step O can begin.
Step S must be finished before step O can begin.
Step K must be finished before step C can begin.
Step N must be finished before step Q can begin.
Step L must be finished before step E can begin.
Step L must be finished before step Z can begin.
Step K must be finished before step W can begin.
Step Y must be finished before step A can begin.
Step L must be finished before step O can begin.
Step N must be finished before step W can begin.
Step R must be finished before step W can begin.
Step C must be finished before step O can begin.
Step H must be finished before step X can begin.
Step V must be finished before step Y can begin.
Step S must be finished before step W can begin.
Step V must be finished before step E can begin.
Step Q must be finished before step E can begin.
Step P must be finished before step H can begin.
Step V must be finished before step H can begin.
Step N must be finished before step Z can begin.
Step C must be finished before step A can begin.
'''
)