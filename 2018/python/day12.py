def solve(a):
	a = a.strip().split("\n")
	a = [x for x in a if len(x)]
	b = list(a[0].split()[2])
	def to_val(mask):
		n = len(mask)
		return sum(1 << (n - 1 - i) for i, x in enumerate(mask) if x == '#')
	f = {}
	for x in a[1:]:
		mask, arrow, out = x.split()
		f[to_val(mask)] = out
	n = len(b)
	for _ in range(200):
		b = ['.'] * 5 + b + ['.'] * 5
		nb = ['.']*len(b)
		for i in range(2, len(b) - 2):
			val = to_val(b[i-2:i+3])
			nb[i] = '.' if val not in f else f[val]
		b = nb
		print("~" * 20)
		print("".join(b))
		print("~" * 20)

	ans = sum(i - 5 * 20 for i, x in enumerate(b) if x == '#')
	print("Part 1:", ans)
	
# solve(
# '''
# initial state: #..#.#..##......###...###

# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #
# '''
# )


solve(
'''
initial state: ###......#.#........##.###.####......#..#####.####..#.###..#.###.#..#..#.#..#..#.##...#..##......#.#

..#.# => .
#..## => #
..### => .
###.# => .
#...# => #
###.. => #
.##.# => #
#..#. => #
#.##. => #
####. => .
.#.## => #
...#. => .
.#..# => #
.###. => .
##..# => #
.##.. => #
.#### => #
.#.#. => #
##### => .
#.#.# => #
...## => #
..##. => .
....# => .
##... => .
##.#. => #
..#.. => #
..... => .
##.## => .
#.### => .
#.#.. => .
.#... => #
#.... => .
'''
)