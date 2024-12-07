from collections import Counter, OrderedDict
def solve1(s):
	s = s.strip().split("\n")
	total = 0
	for line in s:
		x = line[:line.rindex('-')].split("-")
		x = ''.join(x)

		x = Counter(x).most_common()
		x = sorted(x, key=lambda k: (-k[1], k[0]))[:5]
		x = ''.join(map(lambda k: k[0], x))
		# print(line, x, line[line.rindex("[")+1:-1])
		sec = int(line[line.rindex('-') + 1: line.find("[")])
		if x == line[line.rindex("[")+1:-1]:
			total += sec
	print("Part 1:", total)

def solve2(s):
	def shift(ch, n):
		if ch == '-': return ' '
		v = ord(ch) - ord('a')
		v = (v + n) % 26
		return chr(v + ord('a')) 
	s = s.strip().split("\n")
	for line in s:
		x = line[:line.rindex('-')].split("-")
		x = ''.join(x)
		x = Counter(x).most_common()
		x = sorted(x, key=lambda k: (-k[1], k[0]))[:5]
		x = ''.join(map(lambda k: k[0], x))
		sec = int(line[line.rindex('-') + 1: line.find("[")])
		if x == line[line.rindex("[")+1:-1]:
			z = [shift(ch, sec) for ch in line[:line.rindex("-")]]
			z = ''.join(z)
			if "north" in z:
				print("Part 2:", sec)


def solve(s):
	solve1(s)
	solve2(s)

with open('../inputs/day04input.txt') as f:
  s = f.read()
solve(s)