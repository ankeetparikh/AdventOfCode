from collections import defaultdict

def solve1(s):
	s = s.strip().split("\n")
	z = {
		'a':0,
		'b':0,
		'c':0,
		'd':0,
	}
	i = 0
	n = len(s)
	while i < n:
		a, b, *c = s[i].split()
		if a == 'cpy':
			z[c[0]] = z[b] if b in z else int(b)
		if a == 'inc':
			z[b] += 1
		if a == 'dec':
			z[b] -= 1
		if a == 'jnz':
			v = z[b] if b in z else int(b)
			if v == 0: i += 1
			else: i += int(c[0])
			continue
		i += 1
	print("Part 1:", z['a'])

def solve2(s):
	s = s.strip().split("\n")
	z = {
		'a':0,
		'b':0,
		'c':1,
		'd':0,
	}
	i = 0
	n = len(s)
	while i < n:
		a, b, *c = s[i].split()
		if a == 'cpy':
			z[c[0]] = z[b] if b in z else int(b)
		if a == 'inc':
			z[b] += 1
		if a == 'dec':
			z[b] -= 1
		if a == 'jnz':
			v = z[b] if b in z else int(b)
			if v == 0: i += 1
			else: i += int(c[0])
			continue
		i += 1
	print("Part 2:", z['a'])

def solve(s):
	solve1(s)
	solve2(s)

# solve(
# '''
# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
# ''')

with open('../inputs/day12input.txt') as f:
  s = f.read()
solve(s)